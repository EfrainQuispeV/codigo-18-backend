from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

#funcion para crea el token

def get_tokens_for_user(user):
    tokens = RefreshToken.for_user(user)

    return {
        'refresh' : str(tokens),
        'access' : str(tokens.access_token)
    }


#esta funcion para validar token
def validate_token (token):
    try: 
        #UnTypedToken: va a decirnos si el token es valido o no
        #si al tratar de verificar que el token sea valido, este no lo es entonces
        #entrar a un error
        UntypedToken(token)
        return True
    except (InvalidToken, TokenError)as e:
        print (e)
        return False
    
def get_payload_from_token (token):
    try:
        return AccessToken(token).payload
    except (InvalidToken, TokenError) as e:
        print(e)
        return None
