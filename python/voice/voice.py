import os
import requests
from pathlib import Path
from openai import OpenAI

# ==================== 配置信息 ====================
API_KEY = os.getenv("MODELVERSE_API_KEY", "pKJ06yxN5hMdCQcUCc0c8a11-9557-4864-908B-981d5240")  # 你的API密钥
BASE_URL = "https://api.modelverse.cn/v1/"  # UCloud API地址
UPLOAD_URL = "https://api.modelverse.cn/v1/audio/voice/upload"  # 上传接口

# ==================== 第一步：上传自定义音色 ====================
def upload_custom_voice(
    audio_path: str,          # 本地音频文件路径
    voice_name: str,          # 音色名称（用于展示）
    model_name: str = "IndexTeam/IndexTTS-2",  # 对应的模型
    emotion_path: str = None   # 可选的情绪参考音频
) -> str:
    """
    上传自定义音色，返回 voice_id
    音频要求：5-30秒，≤20MB，MP3或WAV格式，采样率≥16kHz [citation:1][citation:2]
    """
    # 准备表单数据
    files = {
        'speaker_file': open(audio_path, 'rb')  # 主音色音频文件
    }
    
    data = {
        'name': voice_name,
        'model': model_name
    }
    
    # 如果提供情绪参考音频，一起上传
    if emotion_path:
        files['emotion_file'] = open(emotion_path, 'rb')
    
    # 发送请求
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    
    try:
        print(f"正在上传音色: {voice_name}...")
        response = requests.post(
            UPLOAD_URL,
            headers=headers,
            files=files,
            data=data
        )
        response.raise_for_status()
        
        result = response.json()
        voice_id = result.get('id')  # 格式如：uspeech:xxxx-xxxx-xxxx-xxxx [citation:1][citation:2]
        print(f"✅ 上传成功！音色ID: {voice_id}")
        return voice_id
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 上传失败: {e}")
        if response.text:
            print(f"错误详情: {response.json()}")
        return None
    finally:
        # 关闭文件句柄
        for f in files.values():
            f.close()

# ==================== 第二步：使用自定义音色合成语音 ====================
def synthesize_with_custom_voice(
    voice_id: str,
    text: str,
    output_path: str = "custom_voice_output.wav",
    emotion_text: str = "害怕",  # 可选：情绪描述，如"愉快"
    emotion_weight: float = 0.8  # 可选：情绪强度
):
    """
    使用自定义音色合成语音 [citation:3]
    """
    # 初始化OpenAI风格的客户端
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL
    )
    
    # 准备请求参数
    params = {
        "model": "IndexTeam/IndexTTS-2",
        "voice": voice_id,  # 使用上传得到的ID
        "input": text,
    }
    
    # 如果需要情绪控制，添加扩展参数 [citation:3]
    if emotion_text:
        params["extra_body"] = {
            "emo_control_method": 3,  # 3=基于情绪文本
            "emo_text": emotion_text,
            "emo_weight": emotion_weight,
            "sample_rate": 24000  # 可选：指定采样率
        }
    
    try:
        print(f"正在合成语音...")
        with client.audio.speech.with_streaming_response.create(**params) as response:
            response.stream_to_file(output_path)
        print(f"✅ 合成成功！音频已保存至: {output_path}")
        
    except Exception as e:
        print(f"❌ 合成失败: {e}")

# ==================== 完整使用流程 ====================
if __name__ == "__main__":
    # 1. 上传音色（假设你有一个准备好的音频文件）
    audio_file = "sample1.wav"  # 你的音频文件路径
    if not Path(audio_file).exists():
        print(f"请准备一个5-30秒的WAV/MP3音频文件，保存为: {audio_file}")
        exit()
    
    voice_id = upload_custom_voice(
        audio_path=audio_file,
        voice_name="星极小姐",
        # emotion_path="happy_sample.wav"  # 可选：情绪参考音频
    )
    
    if voice_id:
        print(voice_id)
        # 3. 尝试带情绪控制的合成 [citation:3]
        synthesize_with_custom_voice(
            voice_id=voice_id,
            text="""
            你喘息着的样子真的好可爱，
            被触手紧紧缠住，浑身瘫软无力。
            那副模样，完全是败犬女主角的样子。
            是啊，那张被泪水、鼻涕和口水弄得一塌糊涂的小脸，
            那随着细微的呼吸上下起伏的部位，
            这是在引诱我吗？
            真的非常漂亮呢。
            变成这样的你，
            从今往后，可以永远享受鱼水之欢。
            幸福
            """,
            output_path="test_audio2.wav",
            emotion_text="愉快",
            emotion_weight=0.7
        )