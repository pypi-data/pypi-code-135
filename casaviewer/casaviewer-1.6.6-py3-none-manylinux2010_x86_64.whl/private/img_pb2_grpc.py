# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import img_pb2 as img__pb2


class viewStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.panel = channel.unary_unary(
        '/rpc.img.view/panel',
        request_serializer=img__pb2.NewPanel.SerializeToString,
        response_deserializer=img__pb2.Id.FromString,
        )
    self.hide = channel.unary_unary(
        '/rpc.img.view/hide',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.show = channel.unary_unary(
        '/rpc.img.view/show',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.freeze = channel.unary_unary(
        '/rpc.img.view/freeze',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.unfreeze = channel.unary_unary(
        '/rpc.img.view/unfreeze',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.close = channel.unary_unary(
        '/rpc.img.view/close',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.release = channel.unary_unary(
        '/rpc.img.view/release',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.axes = channel.unary_unary(
        '/rpc.img.view/axes',
        request_serializer=img__pb2.Axes.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.popup = channel.unary_unary(
        '/rpc.img.view/popup',
        request_serializer=img__pb2.PopUp.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.load = channel.unary_unary(
        '/rpc.img.view/load',
        request_serializer=img__pb2.NewData.SerializeToString,
        response_deserializer=img__pb2.Id.FromString,
        )
    self.reload = channel.unary_unary(
        '/rpc.img.view/reload',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.unload = channel.unary_unary(
        '/rpc.img.view/unload',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.restore = channel.unary_unary(
        '/rpc.img.view/restore',
        request_serializer=img__pb2.Restore.SerializeToString,
        response_deserializer=img__pb2.Id.FromString,
        )
    self.colormap = channel.unary_unary(
        '/rpc.img.view/colormap',
        request_serializer=img__pb2.ColorMap.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.colorwedge = channel.unary_unary(
        '/rpc.img.view/colorwedge',
        request_serializer=img__pb2.Toggle.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.datarange = channel.unary_unary(
        '/rpc.img.view/datarange',
        request_serializer=img__pb2.DataRange.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.contourlevels = channel.unary_unary(
        '/rpc.img.view/contourlevels',
        request_serializer=img__pb2.ContourLevels.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.contourthickness = channel.unary_unary(
        '/rpc.img.view/contourthickness',
        request_serializer=img__pb2.ContourThickness.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.contourcolor = channel.unary_unary(
        '/rpc.img.view/contourcolor',
        request_serializer=img__pb2.ContourColor.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.channel = channel.unary_unary(
        '/rpc.img.view/channel',
        request_serializer=img__pb2.SetChannel.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.zoomlevel = channel.unary_unary(
        '/rpc.img.view/zoomlevel',
        request_serializer=img__pb2.SetZoomLevel.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.zoombox = channel.unary_unary(
        '/rpc.img.view/zoombox',
        request_serializer=img__pb2.SetZoomBox.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.output = channel.unary_unary(
        '/rpc.img.view/output',
        request_serializer=img__pb2.Output.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.fileinfo = channel.unary_unary(
        '/rpc.img.view/fileinfo',
        request_serializer=img__pb2.Path.SerializeToString,
        response_deserializer=img__pb2.FileInfo.FromString,
        )
    self.keyinfo = channel.unary_unary(
        '/rpc.img.view/keyinfo',
        request_serializer=img__pb2.Id.SerializeToString,
        response_deserializer=img__pb2.KeyInfo.FromString,
        )
    self.cwd = channel.unary_unary(
        '/rpc.img.view/cwd',
        request_serializer=img__pb2.Path.SerializeToString,
        response_deserializer=img__pb2.Path.FromString,
        )
    self.done = channel.unary_unary(
        '/rpc.img.view/done',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.interactivemask = channel.unary_unary(
        '/rpc.img.view/interactivemask',
        request_serializer=img__pb2.InteractiveMaskOptions.SerializeToString,
        response_deserializer=img__pb2.InteractiveMaskResult.FromString,
        )


class viewServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def panel(self, request, context):
    """create a new panel (which may or may not be immediately 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def hide(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def show(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def freeze(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unfreeze(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def close(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def release(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def axes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def popup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def load(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reload(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unload(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def restore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def colormap(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def colorwedge(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def datarange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def contourlevels(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def contourthickness(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def contourcolor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def channel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def zoomlevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def zoombox(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def output(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def fileinfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def keyinfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def cwd(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def done(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def interactivemask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_viewServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'panel': grpc.unary_unary_rpc_method_handler(
          servicer.panel,
          request_deserializer=img__pb2.NewPanel.FromString,
          response_serializer=img__pb2.Id.SerializeToString,
      ),
      'hide': grpc.unary_unary_rpc_method_handler(
          servicer.hide,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'show': grpc.unary_unary_rpc_method_handler(
          servicer.show,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'freeze': grpc.unary_unary_rpc_method_handler(
          servicer.freeze,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'unfreeze': grpc.unary_unary_rpc_method_handler(
          servicer.unfreeze,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'close': grpc.unary_unary_rpc_method_handler(
          servicer.close,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'release': grpc.unary_unary_rpc_method_handler(
          servicer.release,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'axes': grpc.unary_unary_rpc_method_handler(
          servicer.axes,
          request_deserializer=img__pb2.Axes.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'popup': grpc.unary_unary_rpc_method_handler(
          servicer.popup,
          request_deserializer=img__pb2.PopUp.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'load': grpc.unary_unary_rpc_method_handler(
          servicer.load,
          request_deserializer=img__pb2.NewData.FromString,
          response_serializer=img__pb2.Id.SerializeToString,
      ),
      'reload': grpc.unary_unary_rpc_method_handler(
          servicer.reload,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'unload': grpc.unary_unary_rpc_method_handler(
          servicer.unload,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'restore': grpc.unary_unary_rpc_method_handler(
          servicer.restore,
          request_deserializer=img__pb2.Restore.FromString,
          response_serializer=img__pb2.Id.SerializeToString,
      ),
      'colormap': grpc.unary_unary_rpc_method_handler(
          servicer.colormap,
          request_deserializer=img__pb2.ColorMap.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'colorwedge': grpc.unary_unary_rpc_method_handler(
          servicer.colorwedge,
          request_deserializer=img__pb2.Toggle.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'datarange': grpc.unary_unary_rpc_method_handler(
          servicer.datarange,
          request_deserializer=img__pb2.DataRange.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'contourlevels': grpc.unary_unary_rpc_method_handler(
          servicer.contourlevels,
          request_deserializer=img__pb2.ContourLevels.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'contourthickness': grpc.unary_unary_rpc_method_handler(
          servicer.contourthickness,
          request_deserializer=img__pb2.ContourThickness.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'contourcolor': grpc.unary_unary_rpc_method_handler(
          servicer.contourcolor,
          request_deserializer=img__pb2.ContourColor.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'channel': grpc.unary_unary_rpc_method_handler(
          servicer.channel,
          request_deserializer=img__pb2.SetChannel.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'zoomlevel': grpc.unary_unary_rpc_method_handler(
          servicer.zoomlevel,
          request_deserializer=img__pb2.SetZoomLevel.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'zoombox': grpc.unary_unary_rpc_method_handler(
          servicer.zoombox,
          request_deserializer=img__pb2.SetZoomBox.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'output': grpc.unary_unary_rpc_method_handler(
          servicer.output,
          request_deserializer=img__pb2.Output.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'fileinfo': grpc.unary_unary_rpc_method_handler(
          servicer.fileinfo,
          request_deserializer=img__pb2.Path.FromString,
          response_serializer=img__pb2.FileInfo.SerializeToString,
      ),
      'keyinfo': grpc.unary_unary_rpc_method_handler(
          servicer.keyinfo,
          request_deserializer=img__pb2.Id.FromString,
          response_serializer=img__pb2.KeyInfo.SerializeToString,
      ),
      'cwd': grpc.unary_unary_rpc_method_handler(
          servicer.cwd,
          request_deserializer=img__pb2.Path.FromString,
          response_serializer=img__pb2.Path.SerializeToString,
      ),
      'done': grpc.unary_unary_rpc_method_handler(
          servicer.done,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'interactivemask': grpc.unary_unary_rpc_method_handler(
          servicer.interactivemask,
          request_deserializer=img__pb2.InteractiveMaskOptions.FromString,
          response_serializer=img__pb2.InteractiveMaskResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rpc.img.view', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
