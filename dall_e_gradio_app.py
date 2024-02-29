import gradio as gr
import openai
import datetime
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()


def match_res_n_model(model,resolution,n):
    if model == "dall-e-2":
        n = gr.Slider(minimum=1, maximum=10, step=1, label="Images Requested", value=1, interactive=True)
        return gr.Radio(choices=["256x256", "512x512", "1024x1024"], label="Image Resolution", value="256x256") , n
    else:
        n = gr.Number(value=1, maximum=1, minimum=1, label="Images Requested")
        return gr.Radio(choices=[ "1024x1024"], label="Image Resolution", value="1024x1024"), n
        
        
def generate_images(openai_api_key, output_file_path, prompt, n, resolution, model, style, quality):
    openai.api_key = openai_api_key
    response_text = "Submitting image creation request to OpenAI with the following parameters:\n"
    response_text += f"Prompt: {prompt}\nNumber of images: {n}\nImage resolution: {resolution}\n\n"
    
    try:
        response = openai.images.generate(
            model=model,
            quality=quality,
            style=style,
            prompt=prompt,
            n=n,
            size=resolution
        )
        
        response_text += "Response:\n"
        images_urls = []
        
        for idx in range(0, n):
            url = response.data[idx].url
            images_urls.append(url)
            response_text += f"URL for Image #{idx}: {url}\n"
        
        # Optionally save the response to a file
        if output_file_path != "":   
            with open(output_file_path, "a") as f:
                now = datetime.datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                f.write("-----------------------------\n")
                f.write(date_time + "\n")
                f.write(response_text)
                for url in images_urls:
                    f.write(url + "\n")
        
        return response_text, images_urls
    except openai.OpenAIError as e:
        return f"Error: {str(e)}", []

# Gradio interface components
with gr.Blocks() as app:
    gr.Markdown("## DALL-E Image Creation")
    with gr.Row():
        key = os.environ.get("OPENAI_API_KEY","")
        openai_api_key = gr.Textbox(label="OpenAI Key", type="password", value=key, placeholder="Enter your OpenAI API key...")
        output_file_path = gr.Textbox(label="Save Log File Path (optional)", placeholder="Enter the file path to save the log file...", type="text")
    with gr.Row():
        prompt = gr.Textbox(label="Prompt", placeholder="Enter your prompt here...")
        n = gr.Slider(minimum=1, maximum=10, step=1, label="Images Requested", value=1)
        model = gr.Radio(choices=["dall-e-2", "dall-e-3"], label="Model", value="dall-e-2")
        resolution = gr.Radio(choices=["256x256", "512x512", "1024x1024"], label="Image Resolution", value="256x256")
    with gr.Row():
        quality = gr.Radio(choices=["standard", "hd"], label="Quality", value="standard")
        style = gr.Radio(choices=["natural", "vivid"], label="Style", value="natural")
        
    generate_button = gr.Button("Generate")
    
    with gr.Row():
        result_text = gr.Textbox(label="Response output:", lines=10, interactive=False)
        images_output = gr.Gallery(label="Generated Images")

    # if the model changes to "dall-e-3", we need to change the resolution and n
    model.change(match_res_n_model, [model,resolution,n],[resolution,n])
    generate_button.click(
        generate_images,
        inputs=[openai_api_key, output_file_path, prompt, n, resolution, model, style, quality],
        outputs=[result_text, images_output]
    )


app.launch(share=True)
