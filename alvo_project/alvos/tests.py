from django.test import TestCase
from .models import Alvo
from datetime import date, timedelta
from django.db.utils import IntegrityError

class AlvoModelTest(TestCase):

    def setUp(self):
        """
        Criação de um alvo para usar nos testes.
        """
        self.alvo = Alvo.objects.create(
            nome="Alvo Teste",
            latitude=-23.550520,
            longitude=-46.633308,
            identificador="12345",
            data_expiracao=date(2025, 12, 31)
        )

    def test_alvo_criado_com_sucesso(self):
        """
        Verifica se o alvo foi criado corretamente.
        """
        alvo = self.alvo
        self.assertEqual(alvo.nome, "Alvo Teste")
        self.assertEqual(alvo.latitude, -23.550520)
        self.assertEqual(alvo.longitude, -46.633308)
        self.assertEqual(alvo.identificador, "12345")
        self.assertEqual(alvo.data_expiracao, date(2025, 12, 31))

    def test_string_representation(self):
        """
        Verifica se o método __str__ retorna o valor esperado.
        """
        self.assertEqual(str(self.alvo), "Alvo Teste")

    def test_identificador_unico(self):
        """
        Testa se o identificador do alvo é único. O Django deve lançar um erro de integridade
        se tentarmos criar um alvo com o mesmo identificador.
        """
        with self.assertRaises(IntegrityError):
            Alvo.objects.create(
                nome="Alvo Teste Duplicado",
                latitude=-23.550520,
                longitude=-46.633308,
                identificador="12345",  # Identificador duplicado
                data_expiracao=date(2026, 12, 31)
            )

    def test_latitude_e_longitude_validas(self):
        """
        Testa as validações das coordenadas geográficas.
        Aqui, você pode adicionar validações personalizadas em seu modelo para garantir que as coordenadas
        estejam no intervalo correto (-90 a 90 para latitude, -180 a 180 para longitude).
        """

        # Testando valores de latitude e longitude válidos
        alvo_valido = Alvo(
            nome="Alvo Válido",
            latitude=45.0,
            longitude=-73.0,
            identificador="67890",
            data_expiracao=date(2025, 12, 31)
        )
        try:
            alvo_valido.save()
            self.assertEqual(Alvo.objects.count(), 2)  # Espera-se que o alvo seja salvo
        except Exception as e:
            self.fail(f"Erro ao salvar alvo válido: {e}")

        # Testando valores de latitude e longitude fora do intervalo
        with self.assertRaises(ValueError):
            Alvo.objects.create(
                nome="Alvo Inválido Latitude",
                latitude=100.0,  # Latitude inválida
                longitude=-46.633308,
                identificador="99999",
                data_expiracao=date(2025, 12, 31)
            )

        with self.assertRaises(ValueError):
            Alvo.objects.create(
                nome="Alvo Inválido Longitude",
                latitude=-23.550520,
                longitude=200.0,  # Longitude inválida
                identificador="99999",
                data_expiracao=date(2025, 12, 31)
            )

    def test_data_expiracao_nao_passada(self):
        """
        Testa se a data de expiração é válida, ou seja, se não está no passado.
        """
        # Criando alvo com data de expiração no futuro
        alvo_futuro = Alvo(
            nome="Alvo Expiração Futura",
            latitude=-23.550520,
            longitude=-46.633308,
            identificador="56789",
            data_expiracao=date(2025, 12, 31)
        )
        alvo_futuro.save()

        # Criando alvo com data de expiração no passado
        with self.assertRaises(ValueError):
            Alvo.objects.create(
                nome="Alvo Expirado",
                latitude=-23.550520,
                longitude=-46.633308,
                identificador="54321",
                data_expiracao=date.today() - timedelta(days=1)  # Data expirada
            )

    def test_validacao_data_expiracao(self):
        """
        Testa se a data de expiração é obrigatória e valida.
        """
        alvo_sem_data = Alvo(
            nome="Alvo sem Data",
            latitude=-23.550520,
            longitude=-46.633308,
            identificador="00000",
            data_expiracao=None  # Data expiracao ausente
        )
        with self.assertRaises(ValueError):
            alvo_sem_data.save()

    def test_criacao_com_valores_limite(self):
        """
        Testa a criação de um alvo com valores limite para latitude e longitude.
        """
        alvo_limite = Alvo.objects.create(
            nome="Alvo Limite",
            latitude=90.0,  # Latitude no limite superior
            longitude=-180.0,  # Longitude no limite inferior
            identificador="10001",
            data_expiracao=date(2025, 12, 31)
        )

        self.assertEqual(alvo_limite.latitude, 90.0)
        self.assertEqual(alvo_limite.longitude, -180.0)

        alvo_limite = Alvo.objects.create(
            nome="Alvo Limite",
            latitude=-90.0,  # Latitude no limite inferior
            longitude=180.0,  # Longitude no limite superior
            identificador="10002",
            data_expiracao=date(2025, 12, 31)
        )

        self.assertEqual(alvo_limite.latitude, -90.0)
        self.assertEqual(alvo_limite.longitude, 180.0)

