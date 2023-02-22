# sys.path.append('虚拟环境的地址/引用模块的地址')
import argparse
# metavar 用来生成帮助信息；
# required 表明这个参数是必须有的(不提供就报错)；
# type 表示该参数类型；
# default 表示该参数的默认值；
# dest 指定解析后的参数名称，若未指定，默认情况将中划线转换为下划线
def parse_args():
    parser = argparse.ArgumentParser('ImgNameListGen')
    parser.add_argument("--input-path","-i", metavar=': image file', required=True, type=str, default="C:/input")
    parser.add_argument("--output-path","-o", metavar=':result file', required=False, type=str, default="C:/output")
    print(parser.parse_known_args()) # 有未知的参数不报错,返回一个tuple类型的命名空间和一个保存着余下的未知参数的list
    # 输出:(Namespace(input_path='input', output_path='out'), ['--test', 'ts'])
    # opt = parser.parse_known_args()[0] #只返回tuple类型的命名空间，后边未知参数不返回
    opt = parser.parse_args()
    return opt

def main():
    args = parse_args()
    print(args.input_path) #desh
    print(args.output_path)
    # 输出:
    # input
    # out
    print("end")


if __name__ == '__main__':
    main()