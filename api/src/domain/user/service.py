from src.domain.user.dtos import PermissionDTO, RoleDTO, UserDTO
from src.domain.user.repository import (
    IPermissionRepository,
    IRoleRepository,
    IUserRepository,
)


class RoleService:
    def __init__(self, repository: IRoleRepository):
        self.__repository = repository

    def get_role(self, role_id: int) -> RoleDTO:
        return self.__repository.get_role_by_id(role_id)

    def get_role_list(self) -> list[RoleDTO]:
        return self.__repository.get_role_list()

    def create(self, dto: RoleDTO):
        self.__repository.create(dto)

    def update(self, role_id: int, dto: RoleDTO):
        self.__repository.update(role_id, dto)

    def delete(self, role_id: int):
        self.__repository.delete(role_id)


class PermissionService:
    def __init__(self, repository: IPermissionRepository):
        self.__repository = repository

    def get_permission(self, permission_id: int) -> PermissionDTO:
        return self.__repository.get_permission_by_id(permission_id)

    def get_permission_list(self) -> list[PermissionDTO]:
        return self.__repository.get_permission_list()

    def create(self, dto: PermissionDTO):
        self.__repository.create(dto)

    def update(self, permission_id: int, dto: PermissionDTO):
        self.__repository.update(permission_id, dto)

    def delete(self, permission_id: int):
        self.__repository.delete(permission_id)


class UserService:
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    def get_user(self, user_id: int) -> UserDTO:
        return self.__repository.get_user_by_id(user_id)

    def get_user_list(self) -> list[UserDTO]:
        return self.__repository.get_user_list()

    def create(self, dto: UserDTO):
        self.__repository.create(dto)

    def update(self, user_id: int, dto: UserDTO):
        self.__repository.update(user_id, dto)

    def delete(self, user_id: int):
        self.__repository.delete(user_id)
