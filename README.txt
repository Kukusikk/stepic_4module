создание виртуального окружения
python3 -m venv selenium_env

подгрузка зависимостей
pip install -r requirements.txt

запуск виртуального окружения
source selenium_env/bin/activate

запуск файла с меткой
pytest -m regitration_and_login_user test_product_page.py 
