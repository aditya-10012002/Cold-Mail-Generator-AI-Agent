import argparse
from prompt_builder import build_prompt
from gemini_client import GeminiClient
from post_processor import clean_email


def main():
    parser = argparse.ArgumentParser(description="Generate cold emails via Gemini API")
    parser.add_argument('--company', required=True, help='Target company name')
    parser.add_argument('--role', required=True, help='Recipient role/title')
    parser.add_argument('--purpose', required=True, help='Purpose of the email')
    parser.add_argument('--tone', choices=['Formal', 'Friendly'], default='Formal', help='Tone of the email')
    args = parser.parse_args()

    prompt = build_prompt(args.company, args.role, args.purpose, args.tone)
    client = GeminiClient()
    raw = client.generate(prompt)
    email = clean_email(raw)
    print(email)


if __name__ == '__main__':
    main()