from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy_garden.mapview import MapView, MapMarker

from modules.location import share_location
from modules.sos import send_sos_alert
from modules.safe_route import get_safe_route

class NightSafeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Title
        self.layout.add_widget(Label(text="NightSafe - Stay Safe at Night", font_size=24))
        
        # Real-Time Location Sharing Button
        location_button = Button(text="Share Location", size_hint=(1, 0.2))
        location_button.bind(on_press=self.share_location)
        self.layout.add_widget(location_button)
        
        # Emergency SOS Button
        sos_button = Button(text="Emergency SOS", size_hint=(1, 0.2), background_color=(1, 0, 0, 1))
        sos_button.bind(on_press=self.send_sos)
        self.layout.add_widget(sos_button)
        
        # Safe Route Navigation Button
        route_button = Button(text="Find Safe Route", size_hint=(1, 0.2))
        route_button.bind(on_press=self.show_safe_route)
        self.layout.add_widget(route_button)

        # Placeholder Map View
        self.mapview = MapView(zoom=11, lat=20.5937, lon=78.9629)  # Center on India for now
        self.layout.add_widget(self.mapview)

        return self.layout
    
    def share_location(self, instance):
        # Call location sharing module
        location = share_location()
        if location:
            self.mapview.center_on(location[0], location[1])
            marker = MapMarker(lat=location[0], lon=location[1])
            self.mapview.add_marker(marker)
    
    def send_sos(self, instance):
        # Call SOS alert module
        send_sos_alert()
        popup = Popup(title='SOS Sent', content=Label(text='Emergency alert sent!'), size_hint=(0.8, 0.3))
        popup.open()
    
    def show_safe_route(self, instance):
        # Call safe route module
        safe_route = get_safe_route()
        # Display the safe route (for now, just print or mock it)
        popup = Popup(title='Safe Route', content=Label(text=safe_route), size_hint=(0.8, 0.3))
        popup.open()

if __name__ == "__main__":
    NightSafeApp().run()
