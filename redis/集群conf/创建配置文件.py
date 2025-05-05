# vim_myredis_cluster_redisCluster6381.conf
# vim_myredis_cluster_redisCluster6382.conf
# vim_myredis_cluster_redisCluster6383.conf
# vim_myredis_cluster_redisCluster6384.conf
# vim_myredis_cluster_redisCluster6385.conf
# vim_myredis_cluster_redisCluster6386.conf

import os
import pathlib

def 切换当前目录():
    os.chdir(pathlib.Path(__file__).parent)

def 创建配置文件():
    for i in range(1,7):    
        with open(f"vim_myredis_cluster_redisCluster{6380+i}.conf","w") as f:
            f.write(f"port {6380+i}")   

def 创建配置文件内容():
    for i in range(1, 7):
        port = 6380 + i
        config_content = f'''bind 0.0.0.0
daemonize yes
protected-mode no
port {port}
logfile "/myredis/cluster/cluster{port}.log"
pidfile /myredis/cluster{port}.pid
dir /myredis/cluster
dbfilename dump{port}.rdb
appendonly yes
appendfilename "appendonly{port}.aof"
requirepass 111111
masterauth 111111

cluster-enabled yes
cluster-config-file nodes-{port}.conf
cluster-node-timeout 5000
'''
        with open(f"vim_myredis_cluster_redisCluster{port}.conf", "w") as f:
            f.write(config_content)

if __name__ == "__main__":
    切换当前目录()
    创建配置文件内容()


'''
bind 0.0.0.0
daemonize yes
protected-mode no
port 6381
logfile "/myredis/cluster/cluster6381.log"
pidfile /myredis/cluster6381.pid
dir /myredis/cluster
dbfilename dump6381.rdb
appendonly yes
appendfilename "appendonly6381.aof"
requirepass 111111
masterauth 111111
 
cluster-enabled yes
cluster-config-file nodes-6381.conf
cluster-node-timeout 5000


bind 0.0.0.0
daemonize yes
protected-mode no
port 6382
logfile "/myredis/cluster/cluster6382.log"
pidfile /myredis/cluster6382.pid
dir /myredis/cluster
dbfilename dump6382.rdb
appendonly yes
appendfilename "appendonly6382.aof"
requirepass 111111
masterauth 111111
 
cluster-enabled yes
cluster-config-file nodes-6382.conf
cluster-node-timeout 5000


bind 0.0.0.0
daemonize yes
protected-mode no
port 6381
logfile "/myredis/cluster/cluster6381.log"
pidfile /myredis/cluster6381.pid
dir /myredis/cluster
dbfilename dump6381.rdb
appendonly yes
appendfilename "appendonly6381.aof"
requirepass 111111
masterauth 111111
 
cluster-enabled yes
cluster-config-file nodes-6381.conf
cluster-node-timeout 5000
'''