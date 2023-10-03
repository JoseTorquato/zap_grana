from django.db import models


class WeddingRegistration(models.Model):
    # Informações pessoais
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome Completo")
    street = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rua")
    street_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número")
    neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    zip_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEP")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    state = models.CharField(max_length=2, blank=True, null=True, verbose_name="Estado")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    cell_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Tel. Celular")
    spouse_cell_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Tel. Celular do Cônjuge")
    cpf = models.CharField(max_length=14, blank=True, null=True, verbose_name="CPF")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    profession = models.CharField(max_length=100, blank=True, null=True, verbose_name="Profissão")

    # Informações do evento
    event_date = models.DateField(unique=True, blank=True, null=True, verbose_name="Data do Evento")
    number_of_guests = models.IntegerField(blank=True, null=True, verbose_name="Número de Convidados")
    bride_and_groom_names = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome dos Noivos")

    # Informações de pagamento
    payment_method = models.CharField(max_length=100, blank=True, null=True, verbose_name="Forma de Pagamento")
    best_day_for_monthly_invoice_due = models.IntegerField(blank=True, null=True, verbose_name="Melhor Dia para Vencimento dos Boletos")

    # Instagram Profiles
    bride_instagram_profile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Perfil Instagram da Noiva")
    groom_instagram_profile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Perfil Instagram do Noivo")

    # Status
    PRE_RESERVA = 'pré reserva'
    OCUPADO = 'ocupado'

    CHOICES = (
        (PRE_RESERVA, 'Pré Reserva'),
        (OCUPADO, 'Ocupado'),
    )

    status = models.CharField(
        max_length=15,
        choices=CHOICES,
        default=PRE_RESERVA,  # Defina um valor padrão se necessário
    )
    class Meta:
        verbose_name_plural = "Registros de Casamento"

    def __str__(self):
        return self.bride_and_groom_names 
