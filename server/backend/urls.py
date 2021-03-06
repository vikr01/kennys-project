from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListUser.as_view()),
    path('createuser', views.AddUser.as_view()),
    path('loguser', views.LogUser.as_view()),
    path('getuserinfo', views.GetUserInformation.as_view()),
    path('addcard', views.AddNewCard.as_view()),
    path('getcards/<int:userId>', views.ListCardsByUser.as_view()),
    path('location/<latitude>/<longitude>', views.Location.as_view()),
    path('adddriver', views.AddDriver.as_view()),
    path('updatelocation', views.UpdateDriverLocation.as_view()),
    path('updatestatus', views.UpdateDriverStatus.as_view()),
    path('updatefixedlocation', views.UpdateFixedDriverLocation.as_view()),
    path('updatefixedstatus', views.UpdateFixedDriverStatus.as_view()),
    path('getdriver', views.GetDriver.as_view()),
    path('getdirectioninfo', views.GetDurationAndDistance.as_view()),
    path('getdriverrequests', views.GetRequestByDriverUserId.as_view()),
    path('addriderequest', views.AddRequest.as_view()),
    path('getcustomerrequests', views.GetRequestByRequestId.as_view()),
    path('updaterequest', views.UpdateRequest.as_view()),
    path('getcurrentdriver', views.GetDriverById.as_view()),
    path('updatefirstname', views.UpdateUserFirstName.as_view()),
    path('updatelastname', views.UpdateUserLastName.as_view()),
    path('updateemail', views.UpdateUserEmail.as_view()),
    path('addaddress', views.AddNewAddress.as_view()),
    path('getaddresses/<int:userId>', views.ListAddressesByUser.as_view()),
    path('driverstatus', views.GetDriverStatus.as_view()),
]
