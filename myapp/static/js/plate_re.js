//����plate_re.htmlҳ��İ�ť�¼���

// �˳���¼��ť���¼�
// ��ȡ��ťԪ��
let logoutButton = document.getElementById('logoutButton');
// Ϊ��ť��ӵ���¼�����
logoutButton.addEventListener('click', function () {
    // �ض���
    window.location.href = '/plate_re/logout';
});


// չʾʶ�����ݰ�ť���¼�
// ��ȡ��ťԪ��
let displayButton = document.getElementById('displayButton');
// Ϊ��ť��ӵ���¼�����
displayButton.addEventListener('click', function () {
    // ���±�ǩ�д�ҳ��
    window.open('/plate_re/plate_display', '_blank');
});