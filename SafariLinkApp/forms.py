from django import forms
from .models import Member
from .models import BusesAvailable


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'fname', 'lname', 'email', 'password', 'amount_paid','seatNumber','vehicle']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from .models import BusesAvailable

class BookingForm(forms.ModelForm):
    class Meta:
        model = BusesAvailable
        fields = [
            'BusName',
            'From',
            'BusDestination',
            'NuberOfSeats'
        ]

        widgets = {
            'From': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Starting Location'}),
            'BusDestination': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Destination will auto-fill'}),
            'NuberOfSeats': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Seats'}),
        }

    # Use a dropdown for BusName
    BusName = forms.ModelChoiceField(
        queryset=BusesAvailable.objects.all(),  # Populates the dropdown with available buses
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Select a Bus",
        label="Bus Name",
    )



