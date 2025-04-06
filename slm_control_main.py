from slm_control_panel import *
from slm_control import *
import sys
from PyQt5.Qt import pyqtSignal
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''initialise main window and instruments'''
    main_window = Window()
    # meadowlark mode generator
    slm_w_1 = int(1920) / 2  # 1920
    slm_h_1 = int(1152) / 2  # 1152

    # initialize the display
    slm1 = SLMdisplay([2560],
                      [slm_w_1],
                      [slm_h_1],
                      ['SLM1'],
                      isImageLock=False)


    '''connect slot function with signal for main_window'''
    main_window.browse1_signal.connect(lambda path: open_slm1_img(path))
    main_window.browse2_signal.connect(lambda path: open_slm2_img(path))
    main_window.line1_input_signal.connect(lambda path: open_slm1_img_by_ledit(path))
    main_window.line2_input_signal.connect(lambda path: open_slm2_img_by_ledit(path))
    main_window.update1_signal.connect(lambda path: update_slm1(path))
    main_window.update2_signal.connect(lambda path: update_slm2(path))


    '''slot functions'''
    def open_slm1_img(path):
        # Load an image
        image = QPixmap(path)
        new_width = round(image.width()/4)
        new_height = round(image.height()/4)
        scaled_image = image.scaled(new_width, new_height)

        image_upload = QGraphicsPixmapItem(scaled_image)
        main_window.scene1.addItem(image_upload)

        # Enable drag and drop
        image_upload.setFlag(QGraphicsPixmapItem.ItemIsMovable)


    def open_slm2_img(path):
        image = QPixmap(path)
        new_width = round(image.width()/4)
        new_height = round(image.height()/4)
        scaled_image = image.scaled(new_width, new_height)

        image_upload = QGraphicsPixmapItem(scaled_image)
        main_window.scene2.addItem(image_upload)

        # Enable drag and drop
        image_upload.setFlag(QGraphicsPixmapItem.ItemIsMovable)

    def open_slm1_img_by_ledit(path):
        image = QPixmap(path)
        print(path)
        new_width = round(image.width() / 4)
        new_height = round(image.height() / 4)
        scaled_image = image.scaled(new_width, new_height)

        image_upload = QGraphicsPixmapItem(scaled_image)
        main_window.scene1.addItem(image_upload)

        # Enable drag and drop
        image_upload.setFlag(QGraphicsPixmapItem.ItemIsMovable)

    def open_slm2_img_by_ledit(path):
        image = QPixmap(path)
        print(path)
        new_width = round(image.width() / 4)
        new_height = round(image.height() / 4)
        scaled_image = image.scaled(new_width, new_height)

        image_upload = QGraphicsPixmapItem(scaled_image)
        main_window.scene2.addItem(image_upload)

        # Enable drag and drop
        image_upload.setFlag(QGraphicsPixmapItem.ItemIsMovable)

    def update_slm1(path):
        item = main_window.scene1.items()[0]
        x_pos = round(item.x())*4
        y_pos = round(item.y())*4
        if not x_pos:
            x_pos = 0
        if not y_pos:
            y_pos = 0
        print(f'x: {x_pos}; y: {y_pos}')
        phase_array = slm1.generate_img(path, x_pos, y_pos)
        phase_array_np = np.array(phase_array)
        slm1.updateArray('SLM1', phase_array_np)
        print('updated slm1')


    def update_slm2(path):
        item = main_window.scene2.items()[0]
        x_pos = round(item.x()) * 4
        y_pos = round(item.y()) * 4
        if not x_pos:
            x_pos = 0
        if not y_pos:
            y_pos = 0
        print(f'x: {x_pos}; y: {y_pos}')
        phase_array = slm1.generate_img(path, x_pos, y_pos)
        phase_array_np = np.array(phase_array)
        slm1.updateArray('SLM2', phase_array_np)
        print('updated slm2')




    main_window.show()
    sys.exit(app.exec_())