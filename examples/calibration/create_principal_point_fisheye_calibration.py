from kognic.io.model.calibration.camera.principal_point_fisheye_calibration import PrincipalPointFisheyeCalibration
from kognic.io.model.calibration.common import Position, RotationQuaternion
from kognic.io.model.calibration.camera.common import CameraMatrix
from kognic.io.model.calibration.camera.principal_point_fisheye_calibration import PrincipalPoint, LensProjectionCoefficients

def unity_principal_point_fisheye_calibration():
    camera_position = Position(x=0.0, y=0.0, z=0.0)
    camera_rotation = RotationQuaternion(w=1.0, x=0.0, y=0.0, z=0.0)
    camera_matrix = CameraMatrix(fx=3450, fy=3250, cx=622, cy=400)
    principal_point = PrincipalPoint(x=0.0, y=0.0)
    lens_projection_coefficients = LensProjectionCoefficients(c1=0.0, c2=0.0, c3=0.0, c4=0.0)
    return PrincipalPointFisheyeCalibration(
        position=camera_position,
        rotation_quaternion=camera_rotation,
        camera_matrix=camera_matrix,
        principal_point=principal_point,
        lens_projection_coefficients=lens_projection_coefficients,
        image_height=1080,
        image_width=1920,
        field_of_view=180.0
    )