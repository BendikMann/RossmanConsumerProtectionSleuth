from youtube_transcript_api import YouTubeTranscriptApi
from deepmultilingualpunctuation import punctuationmodel
from urllib.parse import urlparse, parse_qs

def get_raw_transcript(id: str):
    transcript = YouTubeTranscriptApi.get_transcript(video_id=id, languages=["en"])

    extract_text = [snip['text'] for snip in transcript]
    spaced_text = " ".join(extract_text)

    return spaced_text


punctuationModel = punctuationmodel.PunctuationModel()


def insert_punctuation(text: str):
    punctuation = punctuationModel.restore_punctuation(text)
    return punctuation


def process_transcript(url: str):
    url = urlparse(url)
    id = parse_qs(url.query)['v'][0]

    raw_transcript = get_raw_transcript(id)

    # I'm not sure if this helps our sampling quality at all.
    # raw_transcript = insert_punctuation(raw_transcript)

    return raw_transcript




if __name__ == "__main__":
    example = process_transcript("https://www.youtube.com/watch?v=ksjzI-8Rz2w")


    pass