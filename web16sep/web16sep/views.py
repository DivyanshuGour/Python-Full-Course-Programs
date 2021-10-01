from django.http import HttpResponse

def fun1(request):
    return HttpResponse(""" 
                <html>
                    <head>
                    </head>
                    <body>
                        <h1>Home Page</h1>
                        <hr>
                        <a href="/">Home</a>&nbsp;
                        <a href="/help">Help</a>&nbsp;
                    </body>
                </html>
    """)

def fun2(request):
    return HttpResponse(""" 
                <html>
                    <head>
                    </head>
                    <body>
                        <h1>Help Page</h1>
                        <hr>
                        <a href="/">Home</a>&nbsp;
                        <a href="/help">Help</a>&nbsp;
                    </body>
                </html>
    """)
