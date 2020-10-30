
from rest_framework.views import APIView
from rest_framework.response import Response
from taskapp.models import Employee

class Empdata(APIView):
    def get(self, request, format=None):
        try:
            qs = Employee.objects.all()
            data = []
            for i in qs:
                if i.manager_id != None:
                    emp = {}
                    emp['id'] = i.id
                    emp['emp_name'] = i.emp_name
                    emp['manager_name'] = i.manager_id.emp_name
                    data.append(emp)
                else:
                    pass
            return Response({
                "success": True,
                "message": data

            })

        except Exception as e:
            return Response({
                "success": False,
                "message": "Error happened!!",
                "errors": str(e)
            })
