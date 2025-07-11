# コマンドライン引数として受け取ったdocsなどからそれにふくまれるすべての画像データを別ファイルに抽出する
import sys
import zipfile

class MsOfficeDocument:
    def __init__(self, filename):
        self.filename = filename
        self.media_dir = None # Excelならxlなど、内部のディレクトリ名
    def get_images(self, target_dir=None):
        if target_dir is None:
            target_dir = self.filename + '_images'

        with zipfile.ZipFile(self.filename, 'r') as zf:
            # 指定されたメディアディレクトリ内のファイルを抽出
            for file_info in zf.infolist():
                if file_info.filename.startswith(self.media_dir + '/'):
                    # 抽出先のパスを決定
                    target_path = f"{target_dir}/{file_info.filename.split('/')[-1]}"
                    with open(target_path, 'wb') as f:
                        f.write(zf.read(file_info.filename))

class MsWordDocument(MsOfficeDocument):
    def __init__(self, filename):
        super().__init__(filename)
        self.media_dir = 'word/media'

class MsExcelDocument(MsOfficeDocument):
    def __init__(self, filename):
        super().__init__(filename)
        self.media_dir = 'xl/media'

class MsPowerPointDocument(MsOfficeDocument):
    def __init__(self, filename):
        super().__init__(filename)
        self.media_dir = 'ppt/media'

def usage():
    pass

def process_args(args):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
