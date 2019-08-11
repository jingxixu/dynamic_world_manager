import world_manager_msgs.srv
import world_manager_msgs.msg
import std_srvs.srv
import rospy


def add_mesh(mesh_name, mesh_filepath, pose_stamped):

    service_proxy = rospy.ServiceProxy("/world_manager/add_mesh",
                                       world_manager_msgs.srv.AddMesh)
    service_proxy.wait_for_service(timeout=5)
    scene_object = world_manager_msgs.msg.SceneObject(mesh_name, mesh_filepath, pose_stamped)
    service_proxy(scene_object)


def add_dynamic_mesh(mesh_name, mesh_filepath, pose_topic):
    service_proxy = rospy.ServiceProxy("/world_manager/add_dynamic_mesh",
                                       world_manager_msgs.srv.AddDynamicMesh)
    service_proxy.wait_for_service(timeout=5)
    dynamic_object = world_manager_msgs.msg.DynamicObject(mesh_name, mesh_filepath, pose_topic)
    service_proxy(dynamic_object)


def add_box(object_name, pose_stamped, edge_length_x, edge_length_y, edge_length_z):
    # type: (str, geometry_msgs.msg.PoseStamped, float, float, float) -> ()
    service_proxy = rospy.ServiceProxy("/world_manager/add_box", world_manager_msgs.srv.AddBox)
    service_proxy.wait_for_service(timeout=5)

    scene_box = world_manager_msgs.msg.SceneBox(object_name, pose_stamped, edge_length_x, edge_length_y, edge_length_z)
    service_proxy(scene_box)


def clear_objects():
    service_proxy = rospy.ServiceProxy("/world_manager/clear_objects",
                                       std_srvs.srv.Empty)
    service_proxy.wait_for_service(timeout=5)
    service_proxy()


def remove_object(object_name):
    service_proxy = rospy.ServiceProxy("/world_manager/remove_object", world_manager_msgs.srv.RemoveObject)
    service_proxy.wait_for_service(timeout=5)
    service_proxy(object_name)


def add_walls():
    service_proxy = rospy.ServiceProxy("/world_manager/add_walls",
                                       std_srvs.srv.Empty)
    service_proxy.wait_for_service(timeout=5)
    service_proxy()


def add_tf(frame_name, pose_stamped):
    service_proxy = rospy.ServiceProxy("/world_manager/add_tf",
                                       world_manager_msgs.srv.AddTF)
    service_proxy.wait_for_service(timeout=5)
    service_proxy(frame_name, pose_stamped)
