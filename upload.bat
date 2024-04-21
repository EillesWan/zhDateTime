python -m build
python -m twine check dist/*
pause
python -m twine upload dist/*
pause
python clean_update.py
pause