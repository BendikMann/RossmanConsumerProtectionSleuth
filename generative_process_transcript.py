import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)


def summarize_transcript(transcript: str):
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {
                "role": "system",
                "content": "You are a detective sleuthing for consumer rights violations in transcribed audio. Summarize this content with a focus to the consumers rights. Focus on the possible consumer right violations and the people, companies, and organizations that help or hurt the cause of protecting consumer rights. Some examples of violations of consumer rights are 'Unsafe Products', 'Misleading labels', 'Materially false advertising', 'Bait & switch pricing', 'Not delivering good after payment', 'Lead in toys', 'Discrimination', 'Remotely deactivate products you own via cloud services', 'Alter a purchased item into a significantly different version after the sale.', 'Gather personal data without adequate disclosure and sell it without proper consent.', and so on."
            },
            {
                "role": "user",
                "content": transcript,
            }
        ]
    )

    summary = response.choices[0].message.content

    return summary