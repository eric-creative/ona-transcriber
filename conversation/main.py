from elevenlabs.client import ElevenLabs
import elevenlabs

client = ElevenLabs(
    api_key=""
)

text = "Hello wold"


def handle_conversation():
    while True:
        audio = client.generate(
            text="Hello! My name is Bella.",
            voice=elevenlabs.Voice(
                voice_id='EXAVITQu4vr4xnSDxMaL',
                settings=elevenlabs.VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0,
                                                  use_speaker_boost=True)
            )
        )
        elevenlabs.play(audio)


if __name__ == "__main__":
    handle_conversation()

