import requests
import json
import datetime
x = requests.get('http://127.0.0.1:8000/postapi/').json()
print(type(x))
now = datetime.datetime.now()
print(now)
for m in x:
    title = m.get('title')
    text = m.get('text')
    auth = m.get('author')
    print(title + '\n')
    print(text + '\n')
    print(auth)
    print('\n\n\n')
    
def search(request):
    p = Post.objects.all()
    u = User.objects.all()
    pr = Profile.objects.all()
    if request.method =='POST':
        s_form = SearchForm(request.POST)
        search_keyword = s_form.cleaned_data.get('your_search')
        try:
            blo = p.get(title = search_keyword)
            us = u.get(username = search_keyword)
            u_pk = us.pk
            
        blo_d = blo.title
        pr_data = pr.get(user = u_pk)
        pr_i_d = os.path.join('/media/swai/B4B6-16491/dprogs/my-first-blog-master/media' ,pr_data.image)
        pr_u_d = pr_data.user
        if blo_d == None and pr_i_d == None and pr_u_d == None:
            context = {
                'results': 'No results found for your search'
            }
        else:
            context = {
                'results': 'Search results:',
                'blo_d': blo_d,
                'pr_i_d': str(pr_i_d),
                'pr_u_d': str(pr_u_d),
            }
        print(context.get('results'))