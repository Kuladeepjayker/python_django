from django.shortcuts import render
from .models import Post

posts = [
    {
        "ok": True,
        "members": [{
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [{
                "start_time": "Feb 1 2020  1:33PM",
                "end_time": "Feb 1 2020 1:54PM"
            },
                {
                    "start_time": "Mar 1 2020  11:11AM",
                    "end_time": "Mar 1 2020 2:00PM"
                },
                {
                    "start_time": "Mar 16 2020  5:33PM",
                    "end_time": "Mar 16 2020 8:02PM"
                }
            ]
        },
            {
                "id": "W07QCRPA4",
                "real_name": "Glinda Southgood",
                "tz": "Asia/Kolkata",
                "activity_periods": [{
                    "start_time": "Feb 1 2020  1:33PM",
                    "end_time": "Feb 1 2020 1:54PM"
                },
                    {
                        "start_time": "Mar 1 2020  11:11AM",
                        "end_time": "Mar 1 2020 2:00PM"
                    },
                    {
                        "start_time": "Mar 16 2020  5:33PM",
                        "end_time": "Mar 16 2020 8:02PM"
                    }
                ]
            }
        ]
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
