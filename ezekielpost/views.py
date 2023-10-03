from django.views import generic
from django.shortcuts import redirect
from .models import Post, Department, STAGE, Profile


class PostList(generic.ListView):
    # template name
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs) 
        list_of_case_studies = Post.objects.filter(status=1,type='featured').order_by('-created_on')
        list_of_department = Department.objects.all # used for main and footer menu
        context['list_of_case_studies'] = list_of_case_studies[:5]
        context['list_of_department'] = list_of_department # used for main and footer menu
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs) 
        print(context)
        related_blog_post_by_department = Post.objects.filter(status=1, type= self.object.type, department=self.object.department).order_by('-created_on').exclude(title=self.object.title)
        context['related_blog_post_by_department'] = related_blog_post_by_department[:5]
        return context


class DepartmentDetail(generic.DetailView):
    model = Department
    template_name = 'department_details.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetail, self).get_context_data(**kwargs)
        list_of_department = Department.objects.all # used for main and footer menu
        context['list_of_department'] = list_of_department # used for main and footer menu
        return context


class DepartmentList(generic.ListView):
    model = Department
    template_name = 'departments.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentList, self).get_context_data(**kwargs)
        post_list = Post.objects.filter(status=1).order_by('-created_on')[:3]
        context['post_list'] = post_list
        list_of_department = Department.objects.all # used for main and footer menu
        context['list_of_department'] = list_of_department # used for main and footer menu
        return context


class ProfileList(generic.ListView):
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileList, self).get_context_data(**kwargs)
        user_post_list = Post.objects.filter(status=self.id).order_by('-created_on')[:3]
        context['user_post_list'] = user_post_list
        return context

class ProfileDetail(generic.DetailView):
    model = Profile
    template_name = 'profile_list.html'

def redirect_view(request):
    author = Post.author
    response = redirect('/%s/' % author)
    return response
