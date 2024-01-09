print("Content-Type:text/html; charset=utf-8")
print()
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moteur de recherche en python</title>
    <link rel="stylesheet" href="web/home.css">
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="main-title">
                <h2 class="title">Recherchez !</h2>
            </div>
            <form action="web_search.py" method="get" class="form">
                <div class="form-elt">
                    <input type="text" name="query" id="query" class="search" placeholder="Rechercher">
                </div>
                <div class="submit">
                    <button type="submit" class="submiter" id="submiter">Rechercher</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
"""
print(html)