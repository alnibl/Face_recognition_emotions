from deepface import DeepFace
import json


def verify_face(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        with open('result_of_checking.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        if result_dict.get('verified'):
            return 'Лица идентичны. Всего Вам хорошего.'
        return 'Разные лица! Опасность!'

    except Exception as _ex:
        return _ex


def analyze_face(img_path):
    try:

        result_dict = DeepFace.analyze(img_path=img_path, actions=('age', 'gender', 'race', 'emotion'))

        with open('analyze_face.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'Возраст: {result_dict.get("age")}')
        print(f'Пол: {result_dict.get("gender")}')
        print()
        print('Раса:')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')
        print()
        print('Эмоция:')

        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

    except Exception as _ex:
        return _ex


def main():
    # print(verify_face(img_1='image_1/5.jpg', img_2='image_1/6.jpg'))
    analyze_face('image_1/1.jpg')


if __name__ == '__main__':
    main()
