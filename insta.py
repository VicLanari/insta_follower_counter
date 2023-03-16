from app import *

def main():
    insta_url = input("digite o fim do url do usuário(por exemplo em 'instagram.com/exemplo' seria exemplo): ")
    num = get_insta_followers(insta_url)
    return num

if __name__ == "__main__":
    main()
