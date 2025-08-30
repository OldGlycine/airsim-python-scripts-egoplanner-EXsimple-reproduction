import airsim
import re
import numpy as np

def find_target_actors(pattern="A.*"):
    """
    查找场景中匹配指定模式的所有名称含pattern前缀的物体
    """
    # 连接到AirSim
    client = airsim.MultirotorClient()
    client.confirmConnection()
    
    # 获取场景中所有对象
    objects = client.simListSceneObjects()
    
    # 使用正则表达式过滤目标Actor
    target_actors = []
    regex = re.compile(pattern)
    
    for obj_name in objects:
        if regex.match(obj_name):
            try:
                # 获取Actor的位置
                pose = client.simGetObjectPose(obj_name)
                if pose:
                    position = {
                        'name': obj_name,
                        'x': pose.position.x_val,
                        'y': pose.position.y_val,
                        'z': pose.position.z_val
                    }
                    target_actors.append(position)
                    print(f"Found target: {obj_name} at ({position['x']}, {position['y']}, {position['z']})")
            except Exception as e:
                print(f"Error getting pose for {obj_name}: {str(e)}")
    
    return target_actors

# 使用示例
if __name__ == "__main__":
    targets = find_target_actors("WayPoints.*")
    print(f"Found {len(targets)} target actors")