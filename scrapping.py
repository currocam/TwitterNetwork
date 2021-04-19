#!/usr/bin/env python
import tweepy as tw
import pandas as pd



consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


def getUserID(screen_name):
    """Obtiene ID identificativo usuario.

    Parameters
    ----------
    screen_name : str
        Nombre de usuario.

    Returns
    -------
    userID: int
        ID identificativo usuario.

    """
    try:
        user = api.get_user(screen_name)
        userID = user.id_str
        return userID
    except tw.TweepError as error:
        print("No se ha podido encontrar el ID del usuario")
        print(error)
        return None

def getUserName(userID):
    """Obtiene nombre usuario.

    Parameters
    ----------
    userID: int
        ID identificativo usuario.

    Returns
    -------
    screen_name : str
        Nombre de usuario.
    """
    try:
        user = api.get_user(userID)
        userName = user.screen_name
        return userName
    except tw.TweepError as error:
        print(error)
        return None

def getFollowers(userID):
    """Obtiene la lista de los ID de los seguidores de un usuario.

    Parameters
    ----------
    userID: int
        ID identificativo usuario.

    Returns
    -------
    followers : list
        Lista de IDs.

    """
    user = api.get_user(userID)
    followers=[]
    followers_count = user.followers_count
    try:
        for page in tw.Cursor(api.followers_ids, user_id=userID).pages():
            followers.extend(page)
            if followers_count >= 5000:
                break
        return followers
    except tw.TweepError as error:
        print("Ha habido un error obteniendo los seguidores del usuario {0}".format(userID))
        print(error)

if __name__ == "__main__":
    usuario1='' #Usuario cuyo contacto quieres tener
    usuario2='' #Tu usuario
    max_level = 6 #Nieveles de profundidad a considerar

    user1=getUserID(usuario1)
    user2=getUserID(usuario2)
    users_visited = set([usuario2])  # para ver usuarios ya visitados
    users_with_levels = [(usuario2, 0)] # para ver nivel de profundidad
    df = pd.DataFrame(columns=['target','source'])
    try:
        for user, level in users_with_levels:
            if level >= max_level:
                continue
            else:
                users_list = getFollowers(getUserID(user))
                if users_list != None:
                    dic_temp = {}
                    for i, follower in enumerate(users_list):
                        follower = getUserName(follower)
                        users_list[i]=follower
                        dic_temp[follower]=user
                    temp = pd.DataFrame(list(dic_temp.items()),columns = ['target','source'])
                    print(temp.head())
                    df = df.append(temp)
                    df.to_csv("networkOfFollowers.csv")
                    users_list = list(set(users_list) - set(users_visited)) #eliminar duplicados
                    level += 1
                    for new_user in users_list:
                        if new_user != usuario1:
                            users_visited.add(new_user)
                            users_with_levels.append( (new_user, level) )
                        else:
                            raise StopIteration #parar el proceso de búsqueda una vez lo encuentras
    except StopIteration:
        print('¡Lo encontré!')
        print(new_user)
        print(level)
