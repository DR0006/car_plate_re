/*
  2023-09-30 16:34
  �û�: FxDr
  ������: FXX-LEGION
  ���ݿ�: car_plate_re
  Ӧ�ó���: car_plate_re 
*/

-- users�û��������
CREATE TABLE users
(
    id         INT AUTO_INCREMENT PRIMARY KEY,
    username   VARCHAR(255),
    email      VARCHAR(255) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- ע��ʱ�䣬Ĭ��Ϊ��ǰʱ��
);

-- �޸�������ʼֵΪ10001
ALTER TABLE users
    AUTO_INCREMENT = 10001;

-- --------------------------------------------------------------


-- car_plate���Ʊ������洢�û�ʶ����ĳ��Ƶ���Ϣ
CREATE TABLE car_plate
(
    id                 INT AUTO_INCREMENT PRIMARY KEY,
    user_email         VARCHAR(255),                       -- �û�������
    image_url          VARCHAR(255) NOT NULL,              -- ���ڴ洢ͼƬ
    recognition_result VARCHAR(50),
    confidence         FLOAT,                              -- ���Ŷ���
    timestamp          TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- ʱ�������¼ʶ�������ʱ��
);

