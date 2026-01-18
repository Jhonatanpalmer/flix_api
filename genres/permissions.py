from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        ### Logica da permissao
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.has_perm('genres.view_genre')
        
        #### Permissao para criar novos generos
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        
        ### Permissao para atualizar generos (alterar os dados)
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        
        ### Permissao para deletar generos
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False
    
