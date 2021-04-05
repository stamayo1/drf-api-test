from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Enterprise, Code
from .serializers import EnterpriseSerializer, CodeSerializer, EnterpriseNitSerializer

# Create your views here.
class EnterpriseAPIView(APIView): 
    
    def get(self, request, *args, **kwargs):
        ''' Listado de todas las Empresas
        '''
        enterprises = Enterprise.objects.all()
        enterprise_serializer = EnterpriseSerializer(enterprises, many = True)
        return Response(enterprise_serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        ''' Crear una nueva Empresa
        '''
        new_enterprise = EnterpriseSerializer(data = request.data)
        if new_enterprise.is_valid(): 
            new_enterprise.save()
            return Response(new_enterprise.data, status = status.HTTP_201_CREATED)
        else: 
            return Response({'error': 'Error storage data'}, status= status.HTTP_400_BAD_REQUEST)
        

class EnterpriseCodeAPIView(APIView): 
    
    def get(self, request, pk, *args, **kwargs):
        ''' Todos los codigos asociados a una persona By nit
        '''
        code = Code.objects.filter(owner = pk)
        if code: 
            code_serializer = CodeSerializer(code, many=True)
            return Response(code_serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response({'message': 'Not data'}, status=status.HTTP_200_OK)
    
        
class DetailEnterpriseAPIView(APIView):
    
    def get(self, request, pk, *args, **kwargs): 
        ''' Regresa la info individual de una empresa
        '''
        enterprise = Enterprise.objects.filter(id=pk).first()
        enterprise_serializer = EnterpriseSerializer(enterprise)
        return Response(enterprise_serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk, *args, **kwargs):
        ''' Actualizar información de una Empresa de forma parcial o total
        '''
        enterprise = Enterprise.objects.filter(id=pk).first()
        if enterprise: 
            enterprise_serializer = EnterpriseSerializer(enterprise, data = request.data, partial=True)
            if enterprise_serializer.is_valid(): 
                enterprise_serializer.save()
                return Response(enterprise_serializer.data, status=status.HTTP_200_OK)
            else: 
                return Response({'error': 'Error update data'}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
         
         
class CodeAPIView(APIView):
    ''' Crear una nuevo codigo para una empresa
    '''
    
    def get(self, request, *args, **kwargs): 
       ''' Listado de todos los Codigos
       '''
       code = Code.objects.all()
       code_serializer = CodeSerializer(code, many=True)
       return Response(code_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        ''' Crear una nuevo Code
        '''
        new_code = CodeSerializer(data=request.data)
        if new_code.is_valid():
            new_code.save()
            return Response(new_code.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Error storage data'}, status=status.HTTP_400_BAD_REQUEST)
        
              
class DetailCodeAPIView(APIView):
    
    def get(self, request, pk, *args, **kwargs): 
        ''' Regresa un codigo especifico
        '''
        code =Code.objects.filter(id=pk).first()
        code_serializer = CodeSerializer(code)
        return Response(code_serializer.data, status=status.HTTP_200_OK)
        
    
    def patch(self, request, pk, *args, **kwargs):
        ''' Actualizar información de una Empresa de forma parcial o total
        '''
        code = Code.objects.filter(id=pk).first()
        if code: 
            code_serializer = CodeSerializer(code, data = request.data, partial=True)
            if code_serializer.is_valid(): 
                code_serializer.save()
                return Response(code_serializer.data, status=status.HTTP_200_OK)
            else: 
                return Response({'error': 'Error update data'}, status=status.HTTP_400_BAD_REQUEST) 
        else: 
            return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)


class CodeOwnerAPIView(APIView): 
    
    def  get(self, request, pk, *args, **kwargs): 
        code = Code.objects.filter(id=pk).first()
        if code: 
            owner = Enterprise.objects.get(id=code.owner.id)
            owner_serializer = EnterpriseSerializer(owner)
            return Response(owner_serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response({'error':'Not found code'}, status=status.HTTP_400_BAD_REQUEST)


class EnterpriseNitAPIView(APIView): 
    
    def get(self, request, nit, *args, **kwargs): 
        ''' Conseguir una empresa por su nit y sus codigos asociados
        '''
        enterprise = Enterprise.objects.filter(nit = nit).first()
        enterprise_serializer = EnterpriseNitSerializer(enterprise)
        return Response(enterprise_serializer.data, status=status.HTTP_200_OK)
    