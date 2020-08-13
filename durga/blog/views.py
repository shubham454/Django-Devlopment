from django.shortcuts import render,get_object_or_404,HttpResponse
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
# def post_list_view(request):
#     post_list = Post.objects.all()
#     return render(request,'blog/post_list.html',{'post_list':post_list})

def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,1)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list})

# class based viewfor pagination
# from django.views.generic import ListView
# class PostListView(ListView):
#     model=Post
#     paginate_by=1

def post_detail_view(request,post):
    # post = get_object_or_404(Post,slug=post,
    #                         status='Published',
    #                         publish__year=year,
    #                         publish__month=month,
    #                         publish__day=day)
    try :
        post = Post.objects.get(slug=post)
        #post = Post.objects.get(slug=post,status='Published',publish__year=year,publish__month=month,publish__day=day)
        return render(request,'blog/post_detail.html',{"post":post})
    except Post.DoesNotExist:
        print("Query didn't matched")
    return HttpResponse("Query not matched")


# for Email sending
def mail_send_view(request,id):
    post = get_object_or_404(Post,id=id,status='published')
    sent = False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd = forms.cleaned_data
            post_url = request.build_absolute_url(post.get_absolute_url())
            subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'],post.title)
            message="Read Post At:\n{}\n\n{} comments:\n{}".format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'moreshubham11121994@gmail.com',[cd['to']])
            sent=True
        else:
            form = EmailSendForm()
    return render(request,'blog/sharebyemail.html',{'post':post,'form':form,'sent':sent})
