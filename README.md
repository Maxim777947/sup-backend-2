# sup_test

- .gitignore
- README.md
- api/
    - \_\_init\_\_.py
    - manage.py
    - src/
        - \_\_init\_\_.py
        - apps/
            - \_\_init\_\_.py
            - meets/
                - \_\_init\_\_.py
                - admin.py
                - apps.py
                - forms.py
                - repository.py
                - templates/
                    - create_meet_modal.html
                    - meets.html
                - tests.py
                - urls.py
                - views.py
            - projects/
                - \_\_init\_\_.py
                - admin.py
                - apps.py
                - features.py
                - forms.py
                - tags.py
                - task.py
                - tests.py
                - urls.py
                - views.py
            - users/
                - \_\_init\_\_.py
                - admin.py
                - apps.py
                - tests.py
                - views.py
        - config/
            - \_\_init\_\_.py
            - asgi.py
            - settings.py
            - urls.py
            - wsgi.py
        - db.sqlite3
        - domain/
            - custom_user/
            - meet/
                - dtos.py
                - repository.py
                - service.py
            - project/
                - dtos.py
                - repository.py
                - service.py
        - models/
            - \_\_init\_\_.py
            - apps.py
            - choice_classes.py
            - meets.py
            - migrations/
                - 0001_initial.py
                - \_\_init\_\_.py
            - projects.py
            - users.py
        - validators/
            - \_\_init\_\_.py
            - validators.py
- directory_structure.md
- generate_markdown.py
- infrasructure/
    - docker-compose.yaml
- web/
    - static/
        - css/
            - add_style.css
            - input.css
            - output.css
        - images/
        - script/
            - meets.js
            - script.js
