import logging

def init_logging():
    # 定义日志格式
    log_format = '%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    # 创建一个日志器
    logger = logging.getLogger()
    # logger.setLevel(logging.ERROR)  # 设置全局日志级别
    logger.setLevel(logging.INFO)  # 设置全局日志级别

    
    # 创建文件处理器（保存到文件，UTF-8编码）
    file_handler = logging.FileHandler(
        'app_errors.log',
        mode='a',
        encoding='utf-8'
    )
    # file_handler.setLevel(logging.ERROR)  # 文件处理器的日志级别
    file_handler.setLevel(logging.INFO)  # 文件处理器的日志级别
    file_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))
    
    # 创建控制台处理器（输出到屏幕）
    console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.ERROR)  # 控制台处理器的日志级别
    console_handler.setLevel(logging.INFO)  # 控制台处理器的日志级别
    console_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))
    
    # 给日志器添加两个处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


if __name__ == '__main__':
    def risky_operation():
        # 包含中文的错误示例
        raise ValueError("无效的输入：名称不能为空（测试中文显示）")

    init_logging()
    
    try:
        risky_operation()
    except Exception as e:
        # 记录错误，同时输出到控制台和文件
        logging.error(f"操作执行失败: {str(e)}", exc_info=True)
    