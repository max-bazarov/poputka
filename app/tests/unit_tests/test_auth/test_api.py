import pytest
from httpx import AsyncClient
from pydantic import EmailStr


@pytest.mark.parametrize(
    'name,surname,email,password,status_code',
    [
        ('Ivan', 'Ivanov', 'example@example.com', 'Password1!', 201),
        ('Vasya', 'Vasyanov', 'example@example.com', 'Password2!', 400),
        ('Bad', 'Password', 'test@test.com', 'bad_password', 422),
    ],
)
async def test_register_user(
    name: str,
    surname: str,
    email: EmailStr,
    password: str,
    status_code: int,
    async_client: AsyncClient,
):
    response = await async_client.post(
        '/auth/register',
        json={
            'name': name,
            'surname': surname,
            'email': email,
            'password': password,
        },
    )

    print(response)

    assert response.status_code == status_code
