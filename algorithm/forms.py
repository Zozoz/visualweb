from django import forms


class AlgorithmForm(forms.Form):
    algorithm = forms.CharField()
    minSupport = forms.FloatField()
    minConfidence = forms.FloatField()
    datafile = forms.CharField()

    def clean_minSupport(self):
        minSupport = self.cleaned_data['minSupport']
        if minSupport < 0 or minSupport > 1.0:
            raise forms.ValidationError("must be in 0~1")
        return minSupport

    def clean_minConfidence(self):
        minConfidence = self.cleaned_data['minConfidence']
        if minConfidence < 0 or minConfidence > 1.0:
            raise forms.ValidationError("must be in 0~1")
        return minConfidence


