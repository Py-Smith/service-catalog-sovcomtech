#!/bin/bash
# Create Static
#python3 manage.py collectstatic --noinput

# Apply Migration
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic

# Compile locale
#python3 manage.py compilemessages -l en -l ru 
python  manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')"  && \
echo "Superuser created successfully."
# Wait up database
# chmod +x wait-for-it.sh 
# ./wait-for-it.sh  $DB_HOST:$DB_PORT --timeout=1 --strict -- echo "DataBase is up"

# Run server
python3 manage.py runserver 0.0.0.0:8082