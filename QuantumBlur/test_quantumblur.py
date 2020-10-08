from quantumblur import *

eps = 0.01

# heights to test
h0 = {(0,0):1,(0,1):0,(1,0):0,(1,1):1}
h1 = {(0,0):0,(0,1):1,(1,0):1,(1,1):0}

# images to test
p0 = {(0, 0): (148, 114, 64), (0, 1): (148, 113, 63), (0, 2): (113, 83, 44), (0, 3): (103, 68, 34), (0, 4): (176, 96, 47), (0, 5): (158, 125, 75), (0, 6): (145, 117, 70), (0, 7): (133, 102, 58), (1, 0): (144, 112, 63), (1, 1): (110, 78, 40), (1, 2): (60, 25, 5), (1, 3): (204, 96, 41), (1, 4): (255, 124, 56), (1, 5): (181, 111, 59), (1, 6): (141, 114, 67), (1, 7): (132, 103, 59), (2, 0): (112, 80, 43), (2, 1): (58, 25, 8), (2, 2): (98, 44, 16), (2, 3): (142, 95, 66), (2, 4): (201, 109, 57), (2, 5): (128, 59, 22), (2, 6): (133, 99, 59), (2, 7): (59, 47, 26), (3, 0): (113, 76, 40), (3, 1): (45, 20, 8), (3, 2): (150, 74, 32), (3, 3): (202, 105, 50), (3, 4): (166, 79, 35), (3, 5): (150, 73, 29), (3, 6): (93, 56, 28), (3, 7): (93, 78, 56), (4, 0): (133, 97, 56), (4, 1): (44, 19, 4), (4, 2): (125, 59, 24), (4, 3): (219, 117, 53), (4, 4): (171, 83, 37), (4, 5): (143, 70, 28), (4, 6): (82, 50, 26), (4, 7): (74, 62, 43), (5, 0): (172, 151, 117), (5, 1): (41, 13, 0), (5, 2): (187, 87, 36), (5, 3): (140, 88, 60), (5, 4): (191, 106, 59), (5, 5): (150, 71, 28), (5, 6): (124, 90, 51), (5, 7): (60, 48, 27), (6, 0): (238, 229, 211), (6, 1): (119, 94, 55), (6, 2): (58, 25, 8), (6, 3): (191, 90, 39), (6, 4): (250, 122, 56), (6, 5): (192, 113, 59), (6, 6): (141, 112, 66), (6, 7): (130, 107, 60), (7, 0): (246, 238, 213), (7, 1): (196, 175, 122), (7, 2): (191, 166, 127), (7, 3): (71, 49, 17), (7, 4): (138, 89, 28), (7, 5): (168, 129, 78), (7, 6): (145, 116, 68), (7, 7): (144, 133, 70)}
p1 = {(0, 0): (169, 181, 137), (0, 1): (137, 141, 97), (0, 2): (143, 131, 85), (0, 3): (170, 131, 70), (0, 4): (181, 143, 77), (0, 5): (182, 162, 106), (0, 6): (157, 164, 114), (0, 7): (154, 162, 110), (1, 0): (184, 182, 134), (1, 1): (111, 101, 57), (1, 2): (141, 108, 69), (1, 3): (166, 114, 62), (1, 4): (255, 170, 96), (1, 5): (176, 133, 74), (1, 6): (162, 166, 115), (1, 7): (156, 150, 96), (2, 0): (115, 113, 82), (2, 1): (86, 68, 35), (2, 2): (122, 72, 34), (2, 3): (187, 132, 84), (2, 4): (181, 125, 76), (2, 5): (178, 125, 70), (2, 6): (101, 87, 53), (2, 7): (132, 126, 89), (3, 0): (127, 112, 74), (3, 1): (105, 82, 43), (3, 2): (130, 81, 39), (3, 3): (180, 128, 75), (3, 4): (198, 136, 80), (3, 5): (160, 109, 57), (3, 6): (108, 93, 62), (3, 7): (105, 92, 61), (4, 0): (152, 152, 120), (4, 1): (113, 98, 68), (4, 2): (173, 118, 63), (4, 3): (167, 119, 66), (4, 4): (176, 123, 63), (4, 5): (162, 109, 59), (4, 6): (100, 84, 49), (4, 7): (118, 111, 73), (5, 0): (126, 133, 110), (5, 1): (124, 113, 100), (5, 2): (104, 54, 19), (5, 3): (226, 170, 118), (5, 4): (188, 128, 77), (5, 5): (192, 129, 70), (5, 6): (97, 80, 40), (5, 7): (135, 137, 105), (6, 0): (218, 255, 255), (6, 1): (133, 132, 93), (6, 2): (180, 144, 92), (6, 3): (175, 135, 94), (6, 4): (234, 161, 83), (6, 5): (182, 137, 80), (6, 6): (162, 166, 113), (6, 7): (179, 190, 143), (7, 0): (198, 251, 237), (7, 1): (176, 205, 176), (7, 2): (130, 131, 101), (7, 3): (220, 199, 145), (7, 4): (183, 148, 86), (7, 5): (190, 182, 121), (7, 6): (170, 191, 138), (7, 7): (157, 180, 131)}


def _dict2image(pixel):
    img = newimage('RGB',(8,8))
    for x in range(8):
        for y in range(8):
            img.putpixel((x,y),pixel[x,y])
    return img


def _partial_x(qc,fraction):
    for j in range(qc.num_qubits):
        qc.rx(fraction,j)

def height_rotation():

    # correct answers for the rotation we'll do
    rotated = {}
    rotated[0] = {(0, 0): 1.0, (0, 1): 0.2984464104095249, (1, 0): 0.2984464104095249, (1, 1): 1.0}
    rotated[1] = {(0, 0): 0.2984464104095249, (0, 1): 1.0, (1, 0): 1.0, (1, 1): 0.2984464104095249}

    for j,h in enumerate([h0,h1]):

        qc = height2circuit(h)

        # check that the height comes out of the circuit unchanged
        new_h = circuit2height(qc)
        for pos in h:
            assert abs(h[pos]-new_h[pos])<eps

        # check that the rotation works correctly
        _partial_x(qc,0.5)  
        new_h = circuit2height(qc)
        for pos in h:
            assert abs(rotated[j][pos]-new_h[pos])<eps
            
    print('\nTest for rotating heights completed successfully!')

    
def height_swap():
                
    # correct answers for the swap we'll do
    swapped = {}
    swapped[0] = {(0, 0): 1.0, (0, 1): 0.33333333333333315, (1, 0): 0.33333333333333315, (1, 1): 1.0}
    swapped[1] = {(0, 0): 0.33333333333333315, (0, 1): 1.0, (1, 0): 1.0, (1, 1): 0.33333333333333315}

    # check that swap works correctly
    new_h,_ = swap_heights(h0, h1, 1.0/3)
    for pos in h0:
        assert abs(swapped[0][pos]-new_h[pos])<eps
    
    print('Test for swapping heights completed successfully!')

    
def image_rotation():
    
    # rotate image defined by pixel values in p0
    qcs = image2circuits(_dict2image(p0))
    for qc in qcs:
        _partial_x(qc,0.5)
    new_img0 = circuits2image(qcs)
    
    # this should yield the pixel values of p1
    for x in range(8):
        for y in range(8):
            assert new_img0.getpixel((x,y))==p1[x,y]
                
    print('Test for rotating images completed successfully!')

    
def image_swap():
    
    p_mix = {(0, 0): (165, 211, 195), (0, 1): (128, 159, 136), (0, 2): (164, 144, 97), (0, 3): (222, 202, 148), (0, 4): (220, 195, 126), (0, 5): (186, 162, 103), (0, 6): (143, 176, 138), (0, 7): (173, 210, 171), (1, 0): (165, 193, 178), (1, 1): (135, 152, 126), (1, 2): (185, 157, 110), (1, 3): (201, 174, 129), (1, 4): (212, 172, 111), (1, 5): (193, 155, 95), (1, 6): (143, 155, 112), (1, 7): (191, 213, 173), (2, 0): (133, 132, 113), (2, 1): (110, 107, 79), (2, 2): (140, 96, 57), (2, 3): (179, 118, 71), (2, 4): (196, 134, 82), (2, 5): (164, 113, 67), (2, 6): (103, 92, 60), (2, 7): (153, 148, 114), (3, 0): (130, 135, 111), (3, 1): (120, 121, 89), (3, 2): (130, 94, 56), (3, 3): (159, 117, 74), (3, 4): (180, 134, 81), (3, 5): (156, 116, 71), (3, 6): (112, 108, 73), (3, 7): (138, 133, 92), (4, 0): (140, 161, 154), (4, 1): (142, 155, 137), (4, 2): (145, 113, 74), (4, 3): (178, 147, 111), (4, 4): (189, 150, 97), (4, 5): (166, 128, 78), (4, 6): (129, 134, 98), (4, 7): (152, 160, 124), (5, 0): (138, 146, 142), (5, 1): (126, 133, 124), (5, 2): (144, 108, 76), (5, 3): (194, 142, 101), (5, 4): (205, 147, 92), (5, 5): (164, 115, 69), (5, 6): (116, 111, 81), (5, 7): (166, 171, 144), (6, 0): (169, 215, 229), (6, 1): (154, 188, 182), (6, 2): (201, 183, 142), (6, 3): (233, 223, 190), (6, 4): (230, 203, 148), (6, 5): (201, 172, 110), (6, 6): (160, 189, 154), (6, 7): (204, 247, 228), (7, 0): (168, 238, 255), (7, 1): (136, 186, 188), (7, 2): (171, 159, 114), (7, 3): (255, 255, 221), (7, 4): (245, 232, 181), (7, 5): (194, 181, 123), (7, 6): (156, 211, 186), (7, 7): (186, 244, 231)}
    
    # swap images defined by pixel values in p0 and p1
    swap0, swap1 = swap_images(_dict2image(p0),_dict2image(p1),0.5)
  
    # the first image should have the pixel values of p_mix
    for x in range(8):
        for y in range(8):
            assert swap0.getpixel((x,y))==p_mix[x,y]
    
    print('Test for swapping images completed successfully!')


def row_image_swap():
    
    p_mix = {(0, 0): (188, 156, 108), (0, 1): (218, 191, 154), (0, 2): (194, 200, 164), (0, 3): (202, 207, 153), (0, 4): (200, 215, 196), (0, 5): (231, 247, 243), (0, 6): (241, 239, 242), (0, 7): (250, 232, 228), (1, 0): (190, 160, 117), (1, 1): (175, 136, 94), (1, 2): (153, 123, 81), (1, 3): (218, 210, 178), (1, 4): (255, 255, 255), (1, 5): (238, 221, 198), (1, 6): (255, 255, 255), (1, 7): (244, 217, 210), (2, 0): (130, 95, 57), (2, 1): (91, 48, 23), (2, 2): (171, 95, 41), (2, 3): (250, 239, 227), (2, 4): (224, 217, 237), (2, 5): (213, 150, 106), (2, 6): (177, 146, 131), (2, 7): (156, 132, 139), (3, 0): (126, 89, 50), (3, 1): (111, 66, 36), (3, 2): (203, 145, 82), (3, 3): (228, 231, 193), (3, 4): (177, 182, 183), (3, 5): (199, 160, 123), (3, 6): (164, 134, 122), (3, 7): (157, 137, 146), (4, 0): (170, 145, 115), (4, 1): (133, 91, 64), (4, 2): (255, 197, 135), (4, 3): (238, 253, 220), (4, 4): (167, 179, 170), (4, 5): (213, 172, 134), (4, 6): (163, 134, 118), (4, 7): (163, 155, 167), (5, 0): (171, 147, 121), (5, 1): (105, 66, 55), (5, 2): (200, 118, 60), (5, 3): (255, 255, 255), (5, 4): (212, 211, 221), (5, 5): (220, 153, 108), (5, 6): (171, 142, 125), (5, 7): (159, 145, 154), (6, 0): (255, 255, 255), (6, 1): (206, 179, 145), (6, 2): (191, 164, 122), (6, 3): (225, 228, 200), (6, 4): (241, 250, 236), (6, 5): (255, 236, 213), (6, 6): (251, 253, 245), (6, 7): (252, 244, 241), (7, 0): (248, 244, 231), (7, 1): (255, 255, 255), (7, 2): (226, 255, 255), (7, 3): (211, 223, 176), (7, 4): (191, 209, 183), (7, 5): (238, 255, 255), (7, 6): (235, 235, 233), (7, 7): (255, 255, 255)}
    
    # swap images defined by pixel values in p0 and p1
    swap0, swap1 = row_swap_images(_dict2image(p0),_dict2image(p1),0.5)
    
    # the first image should have the pixel values of p_mix
    for x in range(8):
        for y in range(8):
            assert swap0.getpixel((x,y))==p_mix[x,y]
        
    print('Test for row swapping images completed successfully!')


def log_image():
    
    p_log = {(0, 0): (127, 114, 76), (0, 1): (127, 113, 75), (0, 2): (85, 79, 52), (0, 3): (73, 62, 40), (0, 4): (160, 94, 56), (0, 5): (139, 126, 89), (0, 6): (123, 117, 83), (0, 7): (109, 100, 69), (1, 0): (122, 112, 75), (1, 1): (82, 73, 47), (1, 2): (22, 13, 5), (1, 3): (194, 94, 49), (1, 4): (255, 125, 67), (1, 5): (166, 111, 70), (1, 6): (119, 114, 80), (1, 7): (108, 102, 70), (2, 0): (84, 75, 51), (2, 1): (20, 13, 9), (2, 2): (67, 35, 19), (2, 3): (120, 92, 79), (2, 4): (190, 108, 68), (2, 5): (103, 52, 26), (2, 6): (109, 97, 70), (2, 7): (21, 38, 31), (3, 0): (85, 71, 47), (3, 1): (4, 7, 9), (3, 2): (129, 69, 38), (3, 3): (191, 104, 59), (3, 4): (148, 74, 41), (3, 5): (129, 68, 34), (3, 6): (61, 48, 33), (3, 7): (61, 73, 67), (4, 0): (109, 95, 67), (4, 1): (3, 6, 4), (4, 2): (100, 52, 28), (4, 3): (212, 117, 63), (4, 4): (154, 79, 44), (4, 5): (121, 64, 33), (4, 6): (48, 41, 31), (4, 7): (39, 55, 51), (5, 0): (156, 156, 140), (5, 1): (0, 0, 0), (5, 2): (173, 83, 43), (5, 3): (117, 85, 71), (5, 4): (178, 105, 70), (5, 5): (129, 65, 33), (5, 6): (98, 87, 61), (5, 7): (22, 39, 32), (6, 0): (234, 244, 252), (6, 1): (92, 91, 65), (6, 2): (20, 13, 9), (6, 3): (178, 87, 46), (6, 4): (249, 123, 67), (6, 5): (179, 113, 70), (6, 6): (119, 112, 79), (6, 7): (106, 106, 71), (7, 0): (244, 255, 255), (7, 1): (184, 183, 146), (7, 2): (178, 173, 152), (7, 3): (35, 40, 20), (7, 4): (115, 86, 33), (7, 5): (151, 131, 93), (7, 6): (123, 116, 81), (7, 7): (122, 136, 83)}
    
    # log encode and decode image defined by pixel values in p0
    qcs = image2circuits(_dict2image(p0),log=True)
    new_img0 = circuits2image(qcs,log=True)
    
    # this should yield the pixel values of p_log
    for x in range(8):
        for y in range(8):
            assert new_img0.getpixel((x,y))==p_log[x,y]
                
    print('Test for logarithmic encoding and decoding completed successfully!') 

def odd_size():

    # we'll encode and decode a height map that is not square, and whose height and width are not powers of 2
    h = {}
    for x in range(3):
        for y in range(5):
            h[x,y] = float(x+y)/6
    
    # encode and decode height map
    qc = height2circuit(h)
    new_h = circuit2height(qc)
    
    # check that the height comes out of the circuit unchanged
    for pos in h:
        assert abs(h[pos]-new_h[pos])<eps
            
    print('Test for oddly sized height map completed successfully!')

    
height_rotation()
height_swap()
image_rotation()
image_swap()
row_image_swap()
log_image()
odd_size()

print(':)\n')