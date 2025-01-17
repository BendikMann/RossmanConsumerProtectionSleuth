from dotenv import load_dotenv
# this needs to be done before generative_process_transcript because we create the api client globally
load_dotenv()

from create_transcript import process_transcript
from generative_process_transcript import summarize_transcript


if __name__ == "__main__":
    transcript = process_transcript("https://www.youtube.com/watch?v=ksjzI-8Rz2w")

    with open("transcript.txt", "w") as text_file:
        text_file.write(transcript)

    response = summarize_transcript(transcript)

    summary = response

    with open("summary.txt", "w") as text_file:
        text_file.write(summary)


    pass
