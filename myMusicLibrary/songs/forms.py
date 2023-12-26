from django import forms


class SearchForm(forms.Form):
    nume = forms.CharField(required=False)
    album = forms.CharField(required=False)
    artist = forms.CharField(required=False)

    def get_results(self):
        input_data1 = self.cleaned_data['nume']
        input_data2 = self.cleaned_data['album']
        input_data3 = self.cleaned_data['artist']
        results = [input_data1, input_data2, input_data3]  # <-- modify this process as you need
        # ... (your operations for input_data and results here)
        return results
