from django import forms

POSTURE_CHOICES = (
    ('yoga', 'Yoga'),
    ('zumba', 'Zumba'),
    ('pilates', 'Pilates'),
    ('tai chi', 'Tai Chi'),
    ('ergonomics', 'Ergonomics'),
)

STRESS_REDUCTION = (
    ('massage', 'Massage (RMT)'),
    ('fst', 'FST'),
    ('reiki', 'Reiki'),
    ('reflexology', 'Reflexology'),
    ('aromatherapy', 'Aromatherapy'),
)

ATTENTION_FOCUS = (
    ('meditation', 'Meditation'),
    ('mindfulness', 'Mindfulness'),
    ('biofeedback', 'Biofeedback'),
    ('counselling ', 'Counselling'),
    ('nutrition-coaching', 'Nutrition/Health Coaching'),
)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class PractitionerForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)

    email = forms.EmailField()

    city = forms.CharField(max_length=100, required=True)

    posture_and_ergonomics = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=POSTURE_CHOICES,
    )
    stress_reduction = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STRESS_REDUCTION,
    )
    attention_and_focus = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ATTENTION_FOCUS,
    )
    message = forms.CharField(widget=forms.Textarea, required=False)


class OrganizationForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    organization_name = forms.CharField(max_length=100, required=True)
    contact_email = forms.EmailField()
    city = forms.CharField(max_length=100, required=True)

    posture_and_ergonomics = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=POSTURE_CHOICES,
    )
    stress_reduction = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STRESS_REDUCTION,
    )
    attention_and_focus = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ATTENTION_FOCUS,
    )
    message = forms.CharField(widget=forms.Textarea,
                              initial="Please let us know what times work best for you. "
                                      "Example, lunch and learn, after work, in the morning, etc",
                              required=False)
