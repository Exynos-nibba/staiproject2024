import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class NutrientScannerApp(App):
    def build(self):
        # Load your pre-trained model
        self.model = load_model('plant_nutrient_deficiency_detector.h5')  # Replace with your model's filename

        layout = BoxLayout(orientation='vertical')

        # Prediction result
        self.result_label = Label(text="Click the button to load an image", size_hint=(1, 0.2))
        layout.add_widget(self.result_label)

        # Load Image button
        load_button = Button(text="Load and Predict Image", size_hint=(1, 0.1))
        load_button.bind(on_press=self.load_and_predict_image)
        layout.add_widget(load_button)

        return layout

    def load_and_predict_image(self, instance):
        # Specify the path to the image file (you can modify this to your specific image)
        image_path = 'image-asset.jpg'  # Replace with the actual path to the image

        # Update the label to indicate the image is being processed
        self.result_label.text = "Processing image..."

        # Run prediction on the image
        self.predict_deficiency(image_path)

    def predict_deficiency(self, image_path):
        # Load the image and preprocess it
        img = image.load_img(image_path, target_size=(224, 224))  # Ensure size matches model input
        img_array = image.img_to_array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction using the pre-trained model
        predictions = self.model.predict(img_array)

        # Map prediction to nutrient deficiency label
        deficiencies = ['Iron Deficiency', 'Iodine Deficiency', 'Vitamin D Deficiency', 
                        'Vitamin B12 Deficiency', 'Calcium Deficiency', 'Vitamin A Deficiency', 
                        'Magnesium Deficiency']
        
        predicted_index = np.argmax(predictions)
        predicted_deficiency = deficiencies[predicted_index]

        # Update the result label with the prediction
        self.result_label.text = f"Prediction: {predicted_deficiency}"

if __name__ == "__main__":
    NutrientScannerApp().run()
