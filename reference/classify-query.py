# ------------------------------------------api info-----------------------------------------
import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "sk-dGm0cNd8ApWOFxyhA3A96c76572e478f9c9b133f634eEe34"
os.environ["OPENAI_BASE_URL"] = "https://api.xiaoai.plus/v1"
client = OpenAI()
# ------------------------------------------api info-----------------------------------------

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    # temperature=0.1,
    # top_p=0.5,
    # max_tokens=100,
    messages=[
        {"role": "system", "content": (
            "You will be provided with customer service queries. "
            "Classify each query into a primary category and a secondary category. "
            "Provide your output in json format with the keys: primary and secondary."

            "Primary categories: Billing, Technical Support, Account Management, or General Inquiry."

            "Billing secondary categories:"
            "- Unsubscribe or upgrade"
            "- Add a payment method"
            "- Explanation for charge"
            "- Dispute a charge"

            "Technical Support secondary categories:"
            "- Troubleshooting"
            "- Device compatibility"
            "- Software updates"

            "Account Management secondary categories:"
            "- Password reset"
            "- Update personal information"
            "- Close account"
            "- Account security"

            "General Inquiry secondary categories:"
            "- Product information"
            "- Pricing"
            "- Feedback"
            "- Speak to a human."
        )},
        {"role": "user", "content": "I need to get my internet working again."}
    ]
)

print(completion.choices[0])
# print(completion.choices[0].message.content)
# print(completion.id)
# print(completion.model)
