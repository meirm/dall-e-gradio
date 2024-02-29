# DALL-E Image Generator App

This DALL-E Image Generator App is a Python-based application that combines the power of OpenAI's DALL-E models with Gradio to provide a user-friendly interface for generating images from text prompts. Whether you're a developer, artist, or just curious about AI-generated imagery, this app offers an accessible way to explore the capabilities of text-to-image generation.

## Features

- **Custom Image Generation**: Generate images based on textual descriptions using OpenAI's DALL-E models.
- **Flexible Resolution and Model Selection**: Choose between different resolutions and DALL-E models (DALL-E 2 and DALL-E 3) for varied image quality and styles.
- **Quality and Style Options**: Select image quality (standard or HD) and style (natural or vivid) to fine-tune your results.
- **User-Friendly Interface**: Gradio-based web interface for easy interaction without the need for coding.
- **Result Logging**: Option to save generated images' URLs and details to a log file for further reference.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system (Python 3.6 or later is recommended). You will also need an OpenAI API key to use the DALL-E models. Sign up at [OpenAI](https://openai.com/) to obtain your API key.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/meirm/dall-e-gradio.git
   cd dall-e-gradio
   ```

2. **Install Dependencies**

   Install the required Python libraries using pip:

   ```bash
   pip install gradio openai python-dotenv
   ```

3. **Set Up Your `.env` File**

   Create a `.env` file in the root directory of the project and add your OpenAI API key as follows:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the App

Execute the script to start the application:

```bash
python dall_e_gradio_app.py
```

Once the app is running, navigate to the provided URL in your web browser to start generating images.

## Usage

- **Enter Your OpenAI API Key**: If not set up in the `.env` file, you can enter it directly in the interface.
- **Input Your Prompt**: Type in the text prompt for the image you want to generate.
- **Select Model, Resolution, Quality, and Style**: Choose your preferred settings from the available options.
- **Generate Images**: Click the "Generate" button to start the image generation process.
- **View and Save Results**: The generated images will be displayed in the gallery, and details will be logged if a file path is provided.

## Customization and Expansion

The app is designed for customization. You can modify the `generate_images` function to handle different models, resolutions, and styles. The Gradio interface can also be adjusted to include more input fields and options based on your requirements.

## Contributing

Contributions to the DALL-E Image Generator App are welcome. Please feel free to submit pull requests or create issues for bugs, questions, or new features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy generating unique images with the DALL-E Image Generator App!
