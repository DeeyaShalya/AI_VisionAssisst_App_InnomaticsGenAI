VisionAssist 👁️ - AI for Scene Understanding, Text Extraction & Speech for the Visually Impaired 🗣️

Overview 🌟

Welcome to VisionAssist, an innovative solution designed to assist visually impaired individuals by using cutting-edge AI technology. This project leverages Google Gemini API for scene understanding, Tesseract OCR for text extraction, and pyttsx3 for text-to-speech conversion, all integrated into a user-friendly Streamlit web application.

VisionAssist enables users to upload images, receive detailed descriptions of the scenes, interact with an AI-powered chatbot, and have the responses read aloud for a richer, more accessible experience. Whether you're looking for a detailed scene description or need assistance via a chatbot, VisionAssist has it covered.

Key Features 🚀

🔍 Scene Description: Automatically generate detailed descriptions of the uploaded image to help users understand the scene.

🤖 Chatbot Interaction: Engage with an AI-powered chatbot that responds to user queries in natural language.

🔊 Read Aloud: Listen to the scene descriptions and chatbot responses using text-to-speech technology.

🖼️ Image Upload: Easily upload images for analysis and description.

Technologies Used 💻

1. Streamlit 🖥️

Streamlit is a popular open-source framework for building interactive applications with ease. It allows the integration of various Python libraries and is perfect for rapidly deploying machine learning models and AI-based solutions. In VisionAssist, Streamlit is used to create the web-based user interface for uploading images, displaying results, and interacting with the chatbot.

2. Google Gemini API 🤖

The Google Gemini API powers the scene understanding feature of VisionAssist. It uses advanced AI models to analyze uploaded images and generate insightful descriptions. This is crucial for visually impaired users, providing them with AI-generated summaries of the scene in their images.

3. pyttsx3 (Text-to-Speech) 🎤

Pyttsx3 is a Python library for text-to-speech conversion, enabling VisionAssist to read out loud the descriptions generated by AI and chatbot responses. This adds an extra layer of accessibility for visually impaired users, ensuring they can engage with the content audibly.

4. Tesseract OCR 🔠

For extracting any text from images, Tesseract OCR is used. If the uploaded image contains any visible text, Tesseract will extract and display it. This is especially useful for documents, signs, or other written text embedded in the images.

How It Works 🛠️

1. User Uploads an Image 📤

The user begins by uploading an image through the Streamlit interface. The uploaded image can be in JPG, JPEG, or PNG format.

2. Scene Description Generation 🔍

Once an image is uploaded, VisionAssist invokes the Google Gemini API to analyze the image and generate a detailed description. This description includes:

A list of objects detected in the image and their potential purposes.

A general summary of the scene.

Suggestions for actions or precautions for visually impaired users.

This step makes the app powerful by helping users understand the content and context of their surroundings in an easy-to-digest format.

3. Text Extraction (OCR) 🔠

If the image contains any text (like signs, labels, or documents), Tesseract OCR is used to extract the text and display it to the user. This feature is particularly useful for reading text from signs, documents, or product labels.

4. AI Chatbot Interaction 🤖

The AI Chatbot powered by the Google Gemini API is available for interaction. Users can type a message, and the chatbot will respond, providing additional information or answering questions related to the scene or any other query. This feature mimics a real-time conversation, enhancing the user's experience.

5. Read Aloud with Text-to-Speech 🎤

For accessibility, all the scene descriptions and chatbot responses are read aloud using pyttsx3, a Python library that converts text into speech. The speech synthesis happens in a separate thread to ensure the app remains responsive and does not block other actions.

6. User Interface Design 🎨

The application is designed using Streamlit's easy-to-use layout system. It allows seamless uploading of images, easy display of results (descriptions, chatbot messages, etc.), and interaction through buttons for reading aloud and generating scene descriptions.

How to Use VisionAssist 💡

Step-by-Step Guide 📋

Open the Application: Visit the web app where VisionAssist is hosted.

Upload an Image: Use the “Drag and drop or browse an image” feature to upload any image you'd like analyzed.

Generate Scene Description: Once the image is uploaded, click on the 🔍 Describe Scene button to generate a detailed description of the scene.

Interact with the Chatbot: Use the 💬 Chat with AI section to ask the chatbot questions or have a conversation.

Read Aloud: Click the 🔊 Read Aloud Description button to hear the scene description or chatbot responses spoken aloud.

Chatbot Interaction 🤖

The chatbot is powered by an AI language model (Google Gemini). It responds to user queries and provides valuable insights related to the image. It can be used for follow-up questions or for general queries regarding the content of the image.

Scene Description 🔍

The scene description feature uses Google Gemini to detect and interpret the objects, people, and settings in the image. It provides a concise yet detailed account of what the image contains and makes suggestions on actions or safety measures for the visually impaired.

Text-to-Speech 🎤

To enhance accessibility, all text responses generated by the AI and chatbot are read aloud to the user using pyttsx3. This ensures the user can fully engage with the app without needing to read the screen.

Why This Project Matters 🌍

This project aims to bridge the gap between visually impaired individuals and the world around them. By combining advanced AI technology for scene understanding, chatbot interaction, and speech synthesis, VisionAssist provides a complete solution for users who may struggle to perceive their surroundings. Whether it's describing a scene or helping with everyday tasks, this app makes it easier for visually impaired people to gain insights and interact with the world through AI.

Future Enhancements 🔮

While the current version of VisionAssist is a powerful tool, there are several opportunities for improvement:

Multi-Language Support: Adding support for multiple languages to expand the user base.

Object Detection: Integrating more advanced object detection models for even greater accuracy in scene analysis.

Real-Time Integration: Making the application capable of real-time scene analysis for live environments using camera feeds.

Improved Chatbot: Enhancing the chatbot to offer more advanced conversational capabilities, like remembering previous interactions and providing more personalized responses.

Challenges Faced 🏔️

During the development of this project, several challenges were encountered:

Image Quality: Some images with poor lighting or quality presented difficulties in generating accurate scene descriptions. This was tackled by fine-tuning the model’s input data preprocessing.

Speech Synchronization: Ensuring that the text-to-speech engine didn’t block other processes was critical for maintaining a smooth user experience. This was resolved by running the speech synthesis in a separate thread.

Conclusion 🎯

VisionAssist is an exciting and impactful project that showcases the potential of AI in making the world more accessible for visually impaired individuals. By combining powerful APIs, text-to-speech technology, and an intuitive interface, the app provides an inclusive and enriching experience for its users.

Powered By ⚙️

Google Gemini API

Streamlit

pyttsx3 (Text-to-Speech)

Tesseract OCR

Built with ❤️ by Deeya Shalya

Reach Out 👋

If you're interested in discussing this project or collaborating, feel free to reach out via my LinkedIn or email.
