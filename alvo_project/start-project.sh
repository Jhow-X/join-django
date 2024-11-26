#!/bin/bash

# Espera o banco de dados PostgreSQL iniciar completamente
until python manage.py migrate --noinput; do
  echo "Esperando pelo banco de dados..."
  sleep 2
done

# # Aplica as migrações
# python manage.py migrate

# Cria o superusuário Django automaticamente se ele não existir
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', 'hOfYDKspW1ecZ2Y')
EOF

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8000
