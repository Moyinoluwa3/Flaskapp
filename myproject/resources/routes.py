
from .movies import MoviesApi, MovieApi
from ..services.forgetpassword import Changepassword,ForgetPassword
from .auth import SignupApi, LoginApi
 


def initialize_routes(api):
 api.add_resource(MoviesApi, '/api/movies')
 api.add_resource(MovieApi, '/api/movies/<id>')
 api.add_resource(SignupApi, '/api/auth/signup')
 api.add_resource(Changepassword, '/api/auth/changepassword')
 api.add_resource(ForgetPassword, '/api/auth/forget')
 api.add_resource(LoginApi, '/api/auth/login')
 
