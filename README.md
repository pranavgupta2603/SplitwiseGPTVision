
# SplitwiseGPT Vision 🚀

## Introduction 📖

SplitwiseGPT Vision is an innovative web application designed to simplify bill splitting using advanced image processing, OCR technologies, and AI. Built with Streamlit, it combines the power of Pytesseract and GPT-4 vision for image processing and OCR, and utilizes the Splitwise API for splitting bills and adding them to groups.

## Installation 🛠️

1. Clone the repository:
   ```
   git clone https://github.com/pranavgupta2603/SplitwiseGPTVision.git
   ```
2. Navigate to the project directory:
   ```
   cd splitwisegpt-vision
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```


## Configuration 🔧

Before running the application, you need to set up your environment variables. Use the `example.env` file as a template:

1. Rename `example.env` to `.env`.
2. Add your specific keys for the Splitwise API and other necessary configurations as shown in the `.env` file.

## Usage 🖥️

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
2. Upload a bill image in the supported formats (PNG, JPG, JPEG).
3. Select the person who paid the bill.
4. View the extracted bill details and splits.

## Technologies Used 🧰

- **Streamlit**: For creating the web application interface.
- **Pandas & NumPy**: For data manipulation and numerical computations.
- **OpenCV**: For image processing tasks.
- **Pytesseract**: For optical character recognition (OCR).
- **OpenAI**: Integrating AI models for interpreting bill images.

## Contributing 🤝

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b your-branch-name`.
3. Make your changes and commit: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin your-branch-name`.
5. Submit a pull request.

## License 📄

This project is licensed under the [MIT License](LICENSE.md).
